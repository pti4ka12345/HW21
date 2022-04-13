import json

from new_variant.QA import Question


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
