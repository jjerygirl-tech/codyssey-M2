class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def show(self, number):
        print(f"\n[문제 {number}]")
        print(self.question)

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["question"],
            data["choices"],
            data["answer"],
            data.get("hint", ""),
        )


def create_default_quizzes():
    return [
        Quiz(
            "파이썬에서 화면에 글자를 출력할 때 사용하는 함수는?",
            ["input()", "print()", "write()", "display()"],
            2,
            "화면에 결과를 보여주는 함수입니다.",
        ),
        Quiz(
            "파이썬에서 문자열 자료형을 나타내는 것은?",
            ["str", "int", "bool", "list"],
            1,
            "글자나 문장을 저장하는 자료형입니다.",
        ),
        Quiz(
            "사용자의 입력을 받는 파이썬 함수는?",
            ["get()", "scan()", "input()", "read()"],
            3,
            "사용자가 키보드로 입력한 값을 받습니다.",
        ),
        Quiz(
            "조건에 따라 다른 코드를 실행할 때 사용하는 문법은?",
            ["if", "for", "def", "class"],
            1,
            "조건식을 시작할 때 사용하는 키워드입니다.",
        ),
        Quiz(
            "여러 값을 순서대로 저장할 때 사용하는 자료형은?",
            ["bool", "list", "int", "str"],
            2,
            "대괄호로 여러 값을 순서대로 묶을 수 있습니다.",
        ),
    ]
