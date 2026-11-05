from pathlib import Path
from tempfile import TemporaryDirectory

from quiz import create_default_quizzes
from storage import Storage


def test_storage_round_trip():
    original_state_file = Storage.STATE_FILE
    original_backup_file = Storage.BACKUP_FILE

    try:
        with TemporaryDirectory() as temp_directory:
            Storage.STATE_FILE = Path(temp_directory) / "state.json"
            Storage.BACKUP_FILE = Path(temp_directory) / "state.json.bak"

            quizzes = create_default_quizzes()
            history = [
                {
                    "played_at": "2026-11-05 12:00:00",
                    "question_count": 3,
                    "score": 2,
                }
            ]

            Storage.save(quizzes, 4, history)

            loaded_quizzes, best_score, loaded_history = Storage.load([])

            assert len(loaded_quizzes) == 5
            assert best_score == 4
            assert loaded_quizzes[0].hint == quizzes[0].hint
            assert loaded_history == history

    finally:
        Storage.STATE_FILE = original_state_file
        Storage.BACKUP_FILE = original_backup_file


def test_corrupted_file_recovers_from_backup():
    original_state_file = Storage.STATE_FILE
    original_backup_file = Storage.BACKUP_FILE

    try:
        with TemporaryDirectory() as temp_directory:
            Storage.STATE_FILE = Path(temp_directory) / "state.json"
            Storage.BACKUP_FILE = Path(temp_directory) / "state.json.bak"

            quizzes = create_default_quizzes()

            Storage.save(quizzes, None, [])
            Storage.save(quizzes, 4, [])

            Storage.STATE_FILE.write_text(
                "{ 손상된 JSON",
                encoding="utf-8",
            )

            loaded_quizzes, best_score, history = Storage.load([])

            assert len(loaded_quizzes) == 5
            assert best_score is None
            assert history == []
            assert Storage.STATE_FILE.with_suffix(".corrupt.bak").exists()

    finally:
        Storage.STATE_FILE = original_state_file
        Storage.BACKUP_FILE = original_backup_file


if __name__ == "__main__":
    test_storage_round_trip()
    test_corrupted_file_recovers_from_backup()
    print("저장·복원·백업 복구 테스트를 통과했습니다.")