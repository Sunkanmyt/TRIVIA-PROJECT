# Trivia API DOCUMENTATION

Welcome to the Trivia API Developer Documentation where you’ll learn how to build amazing quiz app(s) experiences with the Trivia API.


###  GETTING ALL CATEGORIES ENDPOINT

`GET  '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs, a success value of `true`, and the total number of categories present

```json
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true,
    "total_categories: 6
}
```

###  GETTING ALL QUESTIONS ENDPOINT

`GET '/questions?page=${integer}'`

- Fetches a paginated dictionary of questions of all available categories,  
- Request Arguments: `page` - integer
- Returns: Object including all categories, current category string, an object with 10 paginated questions, total questions, and a success value of ```true```

```json
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": "Null",
    "questions": [
    {
        "answer": "Maya Angelou",
        "category": 4,
        "difficulty": 2,
        "id": 5,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
        "answer": "Muhammad Ali",
        "category": 4,
        "difficulty": 1,
        "id": 9,
        "question": "What boxer's original name is Cassius Clay?"
    },
    {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4,
        "id": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
        "answer": "Edward Scissorhands",
        "category": 5,
        "difficulty": 3,
        "id": 6,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
        "answer": "Brazil",
        "category": 6,
        "difficulty": 3,
        "id": 10,
        "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
        "answer": "Uruguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
        "answer": "George Washington Carver",
        "category": 4,
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?"
    },
    {
        "answer": "Lake Victoria",
        "category": 3,
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
    },
    {
        "answer": "The Palace of Versailles",
        "category": 3,
        "difficulty": 3,
        "id": 14,
        "question": "In which royal palace would you find the Hall of Mirrors?"
    }
    ],
    "success": true,
    "total_questions": 20
}
```

### DELETING A QUESTION ENDPOINT

`DELETE '/questions/<int:id>'`

- Deletes a question by a specified id number (only the question with that id exists) 
- Request Arguments: `id` - integer
- Example Request: `DELETE 'http://127.0.0.1:5000/questions/20'`
- Returns: The id of the deleted question and a success value of `true`

 ```json
    {
        "deleted_question": 20,
        "success": true
    }
```

###  CREATING A NEW QUESTION ENDPOINT

`POST '/questions'`

- Creates a new question using the submitted question and answer text, difficulty and category value 
- Request Body: 

```json
{
  "question": "Heres a new question string",
  "answer": "Heres a new answer string",
  "difficulty": 1,
  "category": 3
}
```

- Returns: A success value of `true`, the id of the newly added question, a list of paginated questions, and the total number of questions

```json
    {
        "new_question": 21,
        "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
         }
        ],
        "success": true,
        "total questions": 20
    }
```

###  SEARCHING FOR A QUESTION ENDPOINT

`POST '/questions/search'`

- Fetches all questions where a substring matches the search_term. 
- Request Body: 

```json
{
  "searchTerm": "Term being searched for"
}
```

- Returns: An array of questions that met the search conditions, total number of questions that met the search term, the current category string, and a success value of `true`

```json
    {
    "current_category": "Null",
    "questions": [
        {
             "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
           "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
        "success": true,
        "total_questions": 2
    }
```


###  GETTING QUESTIONS BY CATEGORY ENDPOINT

`GET '/categories/<int:id>/questions'`
- Fetches all questions where the category id matches the id.
- Request Arguments: `id` - integer 
- Returns: An object with questions for the specified category, total number of questions in that category, current category string, and a success value of `true`
- Example Request: 'http://127.0.0.1:5000/categories/2/questions'
- Example Response:

```json
    {
    "current_category": "Art",
    "questions": [
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
    ],
  "success": true,
  "total_questions": 4
}
```

###  PLAYING QUIZ ENDPOINT

`POST '/quizzes'`
- Fetches a random question to play the quiz
- Request Body:

```json
{
  "previous_questions": [1, 4, 20, 15],
  "quiz_category": "quiz category"
}
```

- Returns: A random question object, and a success value of `true`

```json
    {
        "question": 
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        "success": true
  }
```

## Thank you for choosing to use Trivia API. We hope you find this documentation useful. Cheers to an efficient development 