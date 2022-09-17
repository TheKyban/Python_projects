import html


class Brain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_no = 0
        self.score = 0
        self.current_question = None

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_questions(self):
        self.current_question = self.question_list[self.question_no]
        self.question_no += 1
        question = html.unescape(self.current_question.question)
        return f"Q{self.question_no}. {question}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            return True
        else:
            return False
