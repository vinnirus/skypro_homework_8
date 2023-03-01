import json
import random

import requests
from question import Question

if __name__ == "__main__":
    response = requests.get('https://jsonkeeper.com/b/TXK5', verify=False)
    print(response.content)
    dict_questions = json.loads(response.content)
    questions = []
    for item in dict_questions:
        current_question = Question(item["q"], item["d"],item["a"],item["d"]*10)
        questions.append(current_question)

    for question in questions:
        print(question.text)
        print(question.complexity)
        print(question.correct_answer)

    random.shuffle(questions)
    for question in questions:
        print(question.text)
        print(question.complexity)
        print(question.correct_answer)
