import random
from datetime import datetime

from quiz import Quiz, create_default_quizzes
from storage import Storage


class QuizGame:
    def __init__(self):
        default_quizzes = create_default_quizzes()
        (
            self.quizzes,
            self.best_score,
            self.history,
        ) = Storage.load(default_quizzes)

    def get_number(self, message, minimum, maximum):
        while True:
            try:
                value = input(message).strip()

                if value == "":
                    print("빈 입력입니다. 숫자를 입력해주세요.")
                    continue

                number = int(value)

                if number < minimum or number > maximum:
                    print(
                        f"{minimum}부터 {maximum} 사이의 숫자를 입력해주세요."
                    )
                    continue

                return number

            except ValueError:
                print("숫자만 입력해주세요.")

    def get_required_text(self, message):
        while True:
            value = input(message).strip()

            if value == "":
                print("빈 입력은 사용할 수 없습니다. 다시 입력해주세요.")
                continue

            return value

    def save_data(self):
        Storage.save(self.quizzes, self.best_score, self.history)

    def get_answer(self, quiz):
        hint_used = False

        while True:
            value = input("정답 번호 (힌트: h): ").strip().lower()

            if value in ("h", "hint"):
                if quiz.hint:
                    print(f"힌트: {quiz.hint}")
                    hint_used = True
                else:
                    print("이 문제에는 등록된 힌트가 없습니다.")
                continue

            try:
                answer = int(value)

                if answer < 1 or answer > 4:
                    print("1부터 4 사이의 숫자를 입력해주세요.")
                    continue

                return answer, hint_used

            except ValueError:
                print("정답 번호 또는 h를 입력해주세요.")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        total_available = len(self.quizzes)
        question_count = self.get_number(
            f"몇 문제를 풀까요? (1-{total_available}): ",
            1,
            total_available,
        )
        selected_quizzes = random.sample(self.quizzes, question_count)
        score = 0

        print(f"\n퀴즈를 시작합니다! 총 {question_count}문제입니다.")

        for number, quiz in enumerate(selected_quizzes, start=1):
            quiz.show(number)
            answer, hint_used = self.get_answer(quiz)

            if quiz.is_correct(answer):
                if hint_used:
                    print("정답입니다! 힌트를 사용해 1점 차감됩니다.")
                else:
                    print("정답입니다!")
                    score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        percentage = score / question_count * 100
        played_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        record = {
            "played_at": played_at,
            "question_count": question_count,
            "score": score,
        }
        self.history.append(record)

        print(
            f"\n결과: {question_count}문제 중 {score}점 획득!"
        )
        print(f"점수: {percentage:.0f}점")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

        self.save_data()

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        question = self.get_required_text("문제를 입력하세요: ")
        choices = []

        for number in range(1, 5):
            choice = self.get_required_text(
                f"선택지 {number}를 입력하세요: "
            )
            choices.append(choice)

        answer = self.get_number("정답 번호 (1-4): ", 1, 4)
        hint = input("힌트를 입력하세요 (없으면 Enter): ").strip()

        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        self.save_data()

        print("퀴즈가 추가되었습니다.")

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 ({len(self.quizzes)}개)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        number = self.get_number(
            f"삭제할 퀴즈 번호 (1-{len(self.quizzes)}): ",
            1,
            len(self.quizzes),
        )
        quiz = self.quizzes[number - 1]
        confirm = input(
            f"'{quiz.question}'을(를) 삭제할까요? (y/n): "
        ).strip().lower()

        if confirm in ("y", "yes"):
            self.quizzes.pop(number - 1)

            if not self.quizzes:
                self.best_score = None

            self.save_data()
            print("퀴즈가 삭제되었습니다.")
        else:
            print("삭제를 취소했습니다.")

    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            total = len(self.quizzes)
            percentage = self.best_score / total * 100 if total else 0
            print(
                f"최고 점수: {self.best_score}/{total} "
                f"({percentage:.0f}점)"
            )

    def show_history(self):
        if not self.history:
            print("아직 점수 기록이 없습니다.")
            return

        print(f"\n점수 기록 ({len(self.history)}회)")

        for number, record in enumerate(self.history, start=1):
            question_count = record["question_count"]
            score = record["score"]
            percentage = score / question_count * 100
            print(
                f"{number}. {record['played_at']} - "
                f"{question_count}문제, {score}점 "
                f"({percentage:.0f}점)"
            )
