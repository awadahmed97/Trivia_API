# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET '/questions'
POST '/questions'
DELETE '/questions/<int:question_id>'

also added 
GET '/questions/<int:question_id>'
POST '/questions/search'
GET '/categories/<int:categories_id>'

##########################################################################
GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
##########################################################################
GET '/questions'
- Fetches a dictionary of all the questions and they are ordered by question id
- Request Arguments: None
- Returns: An object with a multiple keys, questions, answer, category, difficulty, id, question.
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    ....
    ]
}
##########################################################################
POST '/questions'
-Posts a question to the database.
-Request arguments: None
-Returns: id created as well as a list of all questions.
{
  "created": 24, 
  "questions": [{
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },]
##########################################################################
DELETE '/questions/<int:question_id>'
-Delets a question from the database, using the questions id number.
-Request arguments: user needs to pass in an id number
-Returns: All questions without the question that was removed and id number of the removed question
{
  "deleted": 24, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
##########################################################################
GET '/questions/<int:question_id>'
-fetches a question with the id number of the question
-Request arguments:user needs to pass an id number
-Returns:the specific question 
{
  "questions": {
    "answer": "Apollo 13", 
    "category": 5, 
    "difficulty": 4, 
    "id": 2, 
    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  }, 
  "success": true
}
##########################################################################
POST '/questions/search'
-post a search term and returns matching questions with the term
-Request arguments:user needs to pass a search term
-Returns:a list of all the matched questions
{
  "questions": {
    "answer": "Apollo 13", 
    "category": 5, 
    "difficulty": 4, 
    "id": 2, 
    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  }
  ...
  , 
  "success": true
}
##########################################################################
GET '/categories/<int:categories_id>'
-fetches a question with the id number of the question
-Request arguments:user needs to pass a category id number
-Returns:questions from a specific category
{
  "current_category": 2, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    ...
}

##########################################################################
POST '/quiz'
-POSTS a game that gives user the questions based on categories.
-Request arguments: None
-Returns:quiz game that gives you questions based on category you entered

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```