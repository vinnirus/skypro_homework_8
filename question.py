class Question:

    def __repr__(self):
        return f"The question is {self.text}. Complication of question is {self.complexity}. \
        Correct answer is {self.correct_answer} "

    def __init__(self,
                 text,
                 complexity,
                 correct_answer,
                 points,
                 is_question_asked=False,
                 user_answer=None
                 ):
        self.text = text
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.is_question_asked = is_question_asked
        self.user_answer = user_answer
        self.points = points

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.complexity * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.correct_answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.text}?\nСложность: {self.complexity}/5'

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.get_points()} баллов'

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ - {self.correct_answer}'
