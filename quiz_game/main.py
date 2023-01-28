import os
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []



for i in question_data:

    q_question = i['text']
    q_answer = i['answer']
    new_question = Question(q_question,q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.sill_has_question():
    quiz.next_question()

os.system('cls')
print('you have completed the game!!')
print(f'your total score is {quiz.score}/{quiz.question_num}')



