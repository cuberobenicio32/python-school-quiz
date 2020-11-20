import random
from question import Question
from questionPrompts import question_prompts

questions = [
    Question(question_prompts[0], "a")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " corrects")

run_quiz(questions)
