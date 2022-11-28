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
        self.database_path = "postgresql://{}:{}@{}/{}".format('student', 'student', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_categories(self):
        result = self.client().get('/categories')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_categories'])

    def test_405_wrong_method_to_get_categories(self):
        result = self.client().put('/categories')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')


    def test_get_questions(self):
        result = self.client().get('/questions')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        
    def test_405_wrong_method_to_get_questions(self):
        result = self.client().put('/questions')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')


    def test_404_get_paginated_questions_error(self):
        result = self.client().get('/questions/?page=500')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    
    def test_delete_question_which_does_not_exist(self):
        result = self.client().delete('/questions/1000')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    def test_add_question(self):
        result = self.client().post('/questions', json={
            'question': 'questioninfo',
            'answer': 'answerinfo',
            'category' : 3,
            'difficulty': 2
        })
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
       
    def test_add_question_error(self):
        result = self.client().put('/questions')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
        

    def test_search_questions_with_result(self):
        result = self.client().post('/questions/search', json={'searchTerm': 'soccer'})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 2)
        

    def test_search_questions_without_result(self):
        result = self.client().post('/questions/search', json={'searchTerm': 'ball'})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual((data['total_questions']), 0)     
    

    def test_get_questions_by_category(self):
        result = self.client().get('/categories/1/questions')
        data = json.loads(result.data)
        
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
    
    def test_get_questions_by_category_error(self):
        result = self.client().get('/categories/1000/questions')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    def test_quiz_question(self):
        result = self.client().post('/quizzes', json={
            "previous_questions": [5, 9], 
            "quiz_category": {'id': 1, 'type': 'Science'}
            })
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertTrue(data['question'])

    def test_quiz_question_error(self):
        result = self.client().post('/quizzes', json={})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()