import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
        'question': 'how are you?',
        'answer': 'good',
        'category': 1,
        'difficulty': 1
        }

        self.new_question1 = {
        'question': 'how are you?',
        'answer': 'good',
        'category': 50,
        'difficulty': 1
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #Get questions expected
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    #Get categories expected
    def test_get_paginated_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))

    #Get questions failure due to too many pages
    def test_404(self):
        result = self.client().get('/questions?page=50',json={'category':1})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    #Get categories failure due to too many pages
    def test_404c(self):
        result = self.client().get('/categories?page=50',json={'category':1})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')

    #Delete expected
    def test_delete_question(self):
        result = self.client().delete('/questions/3')
        data = json.loads(result.data)

        question = Question.query.filter(Question.id == 3).one_or_none()
        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 3)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(question, None)



    #Delete failure
    def test_422(self):
        result = self.client().delete('/questions/100')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')

    #post expected
    def test_create_question(self):
        result = self.client().post('/questions', json=self.new_question)
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))

    #post failure
    def test_create_question_category_not_in_range(self):
        result = self.client().post('/questions', json = self.new_question1)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    #post enpoint questions based on category: expected
    def test_questions_based_category(self):
        res = self.client().get('/categories/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    #post enpoint questions based on category: failed
    def test_questions_based_category(self):
        res = self.client().get('/categories/50')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    #post search expected
    def test_search_expected(self):
        result = self.client().post('/questions/search',json = {"search_term":"the"})
        data = result.get_json()

        self.assertEqual(result.status_code,200)
        self.assertTrue(data['passed'])


    #post search failed
    def test_search_failed(self):
        result = self.client().post('/questions/search', json={'search_term': "gradescope"})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    #post quiz expected
    def test_quiz_for_expected(self):
        result = self.client().post('/quizzes', json={"quiz_category": 2,"previous_questions": [14]})
        data  = result.get_json()

        self.assertEqual(data['success'], True)
        self.assertTrue(data['quiz'])

    #post quiz failure
    def test_quiz_for_failure(self):
        result = self.client().post('/quizzes', json={"quiz_category": 50,"previous_questions": [16]})
        data = result.get_json()
        
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()