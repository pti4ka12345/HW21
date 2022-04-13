import random
from new_variant.functions import read_questions, statistics

questions = read_questions("questions.json")
random.shuffle(questions)

for question in questions:
    print(
        f"Question number {questions.index(question) + 1}. "
        f"Difficulty {question.difficulty}/10. "
        f"Theme: {question.theme}. "
        f"Author: {question.author}")
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


stats = statistics(questions)

print(
    f"That's all! You answered {stats['right_answer']} "
    f"out of {stats['total_questions']} "
    f"questions and earned {stats['total_score']} points")
