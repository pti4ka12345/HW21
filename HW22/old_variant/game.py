import json
import random
from QA import Question


def read_questions(filename):
    question_list = []

    with open(filename, "r", encoding="utf-8") as file:
        questions_dict = json.load(file)

    for key in questions_dict.keys():
        question_list.append(Question(
            text=key,
            author=questions_dict[key]["author"],
            difficulty=questions_dict[key]["difficulty"],
            answers=questions_dict[key]["answers"],
            theme=questions_dict[key]["theme"]
        ))

    return question_list


questions = read_questions("questions.json")

random.shuffle(questions)

for question in questions:
    print(
        f"Question number {questions.index(question) + 1}. Difficulty {question.difficulty}/10. Theme: {question.theme}. Author: {question.author}")
    print(question)

    user_answer = input()

    if user_answer == "stop":
        break


    question.user_answer = user_answer
    question.is_asked = True

    if question.is_correct():
        print(f"Right! You earn {question.score} points")
    else:
        print(f"Wrong! Right answer -  {question.answers[0]}")


def statistics(question_list):
    stats = {
        "total_questions": 0,
        "right_answer": 0,
        "total_score": 0,
    }

    for question in question_list:
        if question.is_asked:
            stats['total_questions'] += 1
            if question.is_right:
                stats['total_score'] += question.score
                stats['right_answer'] += 1

    return stats


stats = statistics(questions)

print(
    f"That's all! You answered {stats['right_answer']} out of {stats['total_questions']} questions and earned {stats['total_score']} points")
