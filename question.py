class Question:

    def __repr__(self):
        return f"The question is {self.text}. Complication of question is {self.complication}"

    def __int__(self,
                text,
                complication,
                correct_answer,
                is_question_asked,
                points
                ):
        self.text = text
        self.complication = complication
        self.correct_answer = correct_answer
        self.is_question_asked = is_question_asked
        self.points = points

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        pass

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        pass

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        pass

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        pass

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        pass
