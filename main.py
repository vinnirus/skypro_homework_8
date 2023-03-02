import json
import random

import requests
from question import Question


def print_game_statistic(game_question_list: list[Question]) -> None:
    total_points = 0
    total_correct_answer = 0
    for each in game_question_list:
        if each.is_correct():
            total_points += each.get_points()
            total_correct_answer += 1
    print(f"""
    Вот и всё!
    Отвечено на {total_correct_answer} вопроса из {len(game_question_list)}
    Набрано баллов: {total_points}
    """)


if __name__ == "__main__":
    # taking questions from json on http-server
    response = requests.get('https://jsonkeeper.com/b/TXK5', verify=False)
    questions_from_json = json.loads(response.content)

    questions = []

    for question_from_json in questions_from_json:
        current_question = Question(question_from_json["q"], int(question_from_json["d"]), question_from_json["a"])
        questions.append(current_question)

    random.shuffle(questions)
    for question in questions:
        question.build_question()
        question.is_question_asked = True
        question.user_answer = input('Ваш ответ:')

        if question.is_correct():
            question.build_positive_feedback()
        else:
            question.build_negative_feedback()

    print_game_statistic(questions)
