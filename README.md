# 파이썬 기초 퀴즈 게임

## 프로젝트 개요

Python 기본 문법을 연습하기 위해 만든 콘솔 퀴즈 게임입니다. 퀴즈 풀기, 추가, 목록, 최고 점수, 삭제, 점수 기록 기능을 제공합니다.

## 주제와 선정 이유

주제는 파이썬 기초입니다. 현재 배우는 함수, 자료형, 조건문, 반복문을 문제로 다시 확인하기 위해 선택했습니다.

## 개발 환경과 실행

- Python 3.10 이상
- Windows PowerShell
- 외부 라이브러리 없이 표준 라이브러리 사용

```powershell
python main.py
```

테스트:

```powershell
python test_quiz.py
python test_storage.py
```

## 메뉴와 보너스 기능

1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수 확인
5. 퀴즈 삭제
6. 점수 기록 보기
7. 종료

퀴즈는 `random.sample()`으로 무작위 출제되며, 시작 전에 문제 수를 선택할 수 있습니다.
풀이 중 `h` 또는 `hint`를 입력하면 힌트를 볼 수 있고, 힌트를 사용해 맞히면 1점이 차감됩니다.
삭제한 문제는 저장 파일에 반영되며, 점수 기록에는 날짜·시간, 문제 수, 점수가 저장됩니다.

## 입력 검증과 예외 처리

`QuizGame`은 빈 입력, 문자 입력, 범위 밖 숫자, `Ctrl+C`, `EOFError`를 처리합니다.
`Storage`는 JSON 읽기·쓰기와 데이터 구조 검증을 담당하며, 입력 검증과 데이터 입출력 책임을 분리했습니다.

## 클래스 역할과 객체지향 설계

- `Quiz`: 문제, 보기, 정답, 힌트와 정답 판정 담당
- `QuizGame`: 게임 진행, 랜덤 출제, 점수, 추가·삭제·히스토리 담당
- `Storage`: JSON 저장·불러오기·백업·복구 담당

클래스를 사용하면 데이터와 관련 동작을 묶고 책임을 분리할 수 있습니다. 함수만 사용하는 방식보다 여러 퀴즈 객체를 관리하고 기능을 확장하기 쉽습니다.

## 기본 문제

`quiz.py`의 `create_default_quizzes()`는 기본 문제 5개를 생성합니다.
`test_quiz.py`는 기본 문제 수가 5개 이상인지, 모든 문제가 보기 4개와 정답 번호를 갖는지 확인합니다.

## 데이터 저장과 복구

`state.json`은 프로젝트 루트에 저장됩니다. 프로그램 시작 시 `Storage.load()`가 읽고, 퀴즈 추가·삭제·풀이 후 `Storage.save()`가 저장합니다.
저장 전 기존 파일은 `state.json.bak`으로 백업합니다. 원본이 손상되면 `state.json.corrupt.bak`으로 보관한 뒤 백업에서 복구하고, 백업도 없으면 기본 퀴즈로 초기화합니다.

```json
{
    "quizzes": [
        {
            "question": "파이썬에서 출력 함수는?",
            "choices": ["input()", "print()", "write()", "display()"],
            "answer": 2,
            "hint": "화면에 결과를 보여줍니다."
        }
    ],
    "best_score": 5,
    "history": [
        {
            "played_at": "2026-11-05 12:00:00",
            "question_count": 5,
            "score": 4
        }
    ]
}
```

JSON은 사람이 읽기 쉽고 리스트·딕셔너리 구조를 표현하기 좋습니다. 다만 파일 전체를 다시 쓰므로 데이터가 수백~수천 건 이상 커지면 성능과 메모리 사용량이 증가할 수 있어 SQLite 같은 데이터베이스가 더 적합합니다.

## 파일 구조와 변경 위치

```text
mission2_quiz/
├── main.py              # 메뉴와 프로그램 시작
├── quiz.py              # Quiz 클래스와 기본 문제
├── game.py              # 게임 기능과 입력 검증
├── storage.py           # JSON 저장·복구
├── test_quiz.py         # 퀴즈 테스트
├── test_storage.py      # 저장·백업 테스트
├── state.json           # 퀴즈·점수·히스토리
└── docs/screenshots/    # 제출 증빙
```

변경 목적별 주요 위치:

| 목적 | 파일 | 메서드 |
|---|---|---|
| 문제·힌트 변경 | `quiz.py` | `Quiz.__init__`, `to_dict` |
| 랜덤·문제 수·점수 | `game.py` | `play_quiz`, `get_answer` |
| 추가·삭제 | `game.py` | `add_quiz`, `delete_quiz` |
| 히스토리 | `game.py` | `play_quiz`, `show_history` |
| 저장·복구 | `storage.py` | `load`, `save`, `_read_file` |
| 메뉴 | `main.py` | `show_menu`, `main` |

## Git 실습

`feature/add-quiz` 브랜치는 퀴즈 추가 기능을 `main`과 분리해 개발하기 위해 사용했습니다. 기능 확인 후 `main`에 병합해 안정된 코드와 개발 중인 코드를 구분했습니다.

실제 커밋 수는 **18개**입니다.

사용한 명령어:

```text
git init
git add
git commit
git push
git pull
git checkout
git clone
```

커밋 메시지는 다음 형식을 사용했습니다.

```text
Feat: 기능 추가
Fix: 오류 수정
Refactor: 구조 개선
Test: 테스트 추가
Docs: 문서·증빙 추가
Data: 저장 데이터 변경
Merge: 브랜치 병합
```

## 증빙 자료

- [메뉴 화면](docs/screenshots/menu.png)
- [퀴즈 풀이](docs/screenshots/play.png)
- [퀴즈 추가](docs/screenshots/add_quiz.png)
- [최고 점수](docs/screenshots/score.png)
- [Git 로그](docs/screenshots/git_log.png)
- [state.json 퀴즈·힌트](docs/screenshots/state_json_quizzes.png)
- [state.json 점수·히스토리](docs/screenshots/state_json_history.png)
- [브랜치 병합과 커밋](docs/screenshots/branch_merge.png)
- [clone·pull 실습](docs/screenshots/clone_pull.png)

## 개선할 수 있는 점

- 문제별 난이도와 카테고리 추가
- 사용자별 점수 저장
- JSON 대신 데이터베이스 사용
