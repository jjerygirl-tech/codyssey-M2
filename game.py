from quiz import Quiz, create_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None

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

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print(f"\n퀴즈를 시작합니다! 총 {len(self.quizzes)}문제입니다.")

        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.show(number)
            answer = self.get_number("정답 번호: ", 1, 4)

            if quiz.is_correct(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(
            f"\n결과: {len(self.quizzes)}문제 중 "
            f"{score}문제 정답!"
        )

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 ({len(self.quizzes)}개)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")