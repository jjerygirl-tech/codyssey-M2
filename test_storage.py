from pathlib import Path
from tempfile import TemporaryDirectory

from quiz import create_default_quizzes
from storage import Storage


def test_storage_round_trip():
    original_state_file = Storage.STATE_FILE

    with TemporaryDirectory() as temp_directory:
        Storage.STATE_FILE = Path(temp_directory) / "state.json"

        quizzes = create_default_quizzes()
        Storage.save(quizzes, 4)

        loaded_quizzes, best_score = Storage.load([])

        assert len(loaded_quizzes) == 5
        assert best_score == 4
        assert loaded_quizzes[0].question == quizzes[0].question

    Storage.STATE_FILE = original_state_file


if __name__ == "__main__":
    test_storage_round_trip()
    print("저장·복원 테스트를 통과했습니다.")