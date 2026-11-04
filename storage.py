import json
from pathlib import Path

from quiz import Quiz


class Storage:
    STATE_FILE = Path("state.json")

    @classmethod
    def load(cls, default_quizzes):
        if not cls.STATE_FILE.exists():
            print("저장된 데이터가 없어 기본 퀴즈를 사용합니다.")
            return default_quizzes, None

        try:
            with cls.STATE_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식이 올바르지 않습니다.")

            quiz_data = data.get("quizzes")
            best_score = data.get("best_score")

            if not isinstance(quiz_data, list):
                raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

            quizzes = []

            for item in quiz_data:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

                question = item.get("question")
                choices = item.get("choices")
                answer = item.get("answer")

                if (
                    not isinstance(question, str)
                    or not question.strip()
                    or not isinstance(choices, list)
                    or len(choices) != 4
                    or not all(isinstance(choice, str) for choice in choices)
                    or not isinstance(answer, int)
                    or answer not in range(1, 5)
                ):
                    raise ValueError("퀴즈 데이터 값이 올바르지 않습니다.")

                quizzes.append(Quiz(question, choices, answer))

            if best_score is not None and (
                not isinstance(best_score, int) or best_score < 0
            ):
                raise ValueError("최고 점수 형식이 올바르지 않습니다.")

            print(
                f"저장된 데이터를 불러왔습니다. "
                f"퀴즈 {len(quizzes)}개"
            )
            return quizzes, best_score

        except (json.JSONDecodeError, OSError, ValueError, KeyError):
            print("저장 파일이 손상되어 기본 퀴즈로 초기화합니다.")
            return default_quizzes, None

    @classmethod
    def save(cls, quizzes, best_score):
        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score,
        }

        try:
            with cls.STATE_FILE.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터를 저장했습니다.")

        except OSError as error:
            print(f"데이터 저장에 실패했습니다: {error}")