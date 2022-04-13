class GenericQuestion():

    def __init__(self, text, author, difficulty, answers, theme, user_answer="", is_asked=False, is_right=True):
        self.text = text
        self.author = author
        self.difficulty = difficulty
        self.answers = answers
        self.theme = theme
        self.is_asked = is_asked
        self.user_answer = user_answer
        self.score = difficulty*10
        self.is_right = is_right

    def __repr__(self):
        return self.text


class Question(GenericQuestion):

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.user_answer in self.answers

    def build_question(self):
        return f"Difficulty: {self.difficulty}, theme: {self.theme} .\nQuestion: \n{self.text}"

