import json
import shutil
from pathlib import Path

from quiz import Quiz


class Storage:
    STATE_FILE = Path("state.json")
    BACKUP_FILE = Path("state.json.bak")

    @classmethod
    def _read_file(cls, file_path):
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("데이터 형식이 올바르지 않습니다.")

        quiz_data = data.get("quizzes")
        best_score = data.get("best_score")
        history_data = data.get("history", [])

        if not isinstance(quiz_data, list):
            raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

        if not isinstance(history_data, list):
            raise ValueError("점수 기록 형식이 올바르지 않습니다.")

        quizzes = []

        for item in quiz_data:
            if not isinstance(item, dict):
                raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

            question = item.get("question")
            choices = item.get("choices")
            answer = item.get("answer")
            hint = item.get("hint", "")

            if (
                not isinstance(question, str)
                or not question.strip()
                or not isinstance(choices, list)
                or len(choices) != 4
                or not all(isinstance(choice, str) for choice in choices)
                or not isinstance(answer, int)
                or answer not in range(1, 5)
                or not isinstance(hint, str)
            ):
                raise ValueError("퀴즈 데이터 값이 올바르지 않습니다.")

            quizzes.append(Quiz(question, choices, answer, hint))

        if best_score is not None and (
            not isinstance(best_score, int) or best_score < 0
        ):
            raise ValueError("최고 점수 형식이 올바르지 않습니다.")

        history = []

        for record in history_data:
            if not isinstance(record, dict):
                raise ValueError("점수 기록 형식이 올바르지 않습니다.")

            played_at = record.get("played_at")
            question_count = record.get("question_count")
            score = record.get("score")

            if (
                not isinstance(played_at, str)
                or not isinstance(question_count, int)
                or question_count < 1
                or not isinstance(score, int)
                or score < 0
            ):
                raise ValueError("점수 기록 값이 올바르지 않습니다.")

            history.append(
                {
                    "played_at": played_at,
                    "question_count": question_count,
                    "score": score,
                }
            )

        return quizzes, best_score, history

    @classmethod
    def _backup_corrupted_file(cls):
        try:
            if cls.STATE_FILE.exists():
                shutil.copyfile(cls.STATE_FILE, cls.STATE_FILE.with_suffix(".corrupt.bak"))
                print("손상된 원본을 state.json.corrupt.bak으로 백업했습니다.")
        except OSError as error:
            print(f"손상 파일 백업에 실패했습니다: {error}")

    @classmethod
    def load(cls, default_quizzes):
        if not cls.STATE_FILE.exists():
            print("저장된 데이터가 없어 기본 퀴즈를 사용합니다.")
            return default_quizzes, None, []

        try:
            quizzes, best_score, history = cls._read_file(cls.STATE_FILE)
            print(
                f"저장된 데이터를 불러왔습니다. "
                f"퀴즈 {len(quizzes)}개, 기록 {len(history)}개"
            )
            return quizzes, best_score, history

        except (json.JSONDecodeError, OSError, ValueError, KeyError):
            print("state.json이 손상되어 백업 파일을 확인합니다.")
            cls._backup_corrupted_file()

            try:
                quizzes, best_score, history = cls._read_file(cls.BACKUP_FILE)
                print("백업 파일에서 데이터를 복구했습니다.")
                return quizzes, best_score, history

            except (json.JSONDecodeError, OSError, ValueError, KeyError):
                print("복구할 백업이 없어 기본 퀴즈로 초기화합니다.")
                return default_quizzes, None, []

    @classmethod
    def save(cls, quizzes, best_score, history):
        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score,
            "history": history,
        }

        try:
            if cls.STATE_FILE.exists():
                shutil.copyfile(cls.STATE_FILE, cls.BACKUP_FILE)

            with cls.STATE_FILE.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터를 저장했습니다.")

        except OSError as error:
            print(f"데이터 저장에 실패했습니다: {error}")