from brain import Brain
from gui import Gui
from question import question_list


questions = question_list
brain = Brain(questions)
ui = Gui(brain)