import html
import requests

api_link = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
response = requests.get(url=api_link)
questions = response.json()["results"]


class QuestionModel:
    def __init__(self, q_list, ans_list):
        self.question = q_list
        self.answer = ans_list


question_list = [QuestionModel(html.unescape(question["question"]), question["correct_answer"]) for question in
                 questions]
