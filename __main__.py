import random
from question import Question
from questionPrompts import question_prompts

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]
random.shuffle(questions)

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
            print("Correct answer!")
        else:
            print(f"Incorrect answer. The {question.answer.upper()} was the right one!")
    print("You got " + str(score) + "/" + str(len(questions)) + " corrects")

run_quiz(questions)
