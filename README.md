# 파이썬 기초 퀴즈 게임

## 프로젝트 개요

Python 기본 문법을 연습하기 위해 만든 콘솔 퀴즈 게임입니다.
메뉴에서 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 최고 점수 확인을 할 수 있습니다.

## 퀴즈 주제와 선정 이유

퀴즈 주제는 파이썬 기초입니다.
현재 배우고 있는 함수, 자료형, 조건문 등의 내용을 문제로 다시 확인하기 위해 이 주제를 선택했습니다.

## 개발 환경

- Python 3.10 이상
- Windows PowerShell
- 외부 라이브러리 없이 Python 표준 라이브러리 사용

## 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```powershell
python main.py
```

자동 테스트는 다음 명령어로 실행합니다.

```powershell
python test_quiz.py
python test_storage.py
```

## 기능 목록

1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 퀴즈 삭제
6. 점수 기록 보기
7. 프로그램 종료

## 보너스 기능

### 랜덤 출제

퀴즈를 풀 때 `random.sample()`을 사용해 선택한 문제 수만큼 문제 순서를 무작위로 섞습니다.

### 문제 수 선택

퀴즈 시작 전에 전체 문제 중 몇 문제를 풀지 선택할 수 있습니다.

### 힌트 기능

각 퀴즈에 힌트를 저장할 수 있습니다. 풀이 중 `h` 또는 `hint`를 입력하면 힌트가 표시됩니다.
힌트를 사용해 정답을 맞히면 해당 문제의 1점이 차감됩니다.

### 퀴즈 삭제

퀴즈 목록에서 번호를 선택해 퀴즈를 삭제할 수 있으며, 삭제 결과는 `state.json`에 저장됩니다.

### 점수 기록 히스토리

게임을 끝낼 때마다 날짜·시간, 푼 문제 수, 점수를 기록합니다.
메뉴의 점수 기록 보기에서 모든 기록을 확인할 수 있습니다.

## 입력 검증과 예외 처리

- 빈 입력 처리
- 숫자가 아닌 입력 처리
- 허용 범위를 벗어난 숫자 처리
- `Ctrl+C`와 `EOFError` 안전 종료
- JSON 파일 손상 시 기본 퀴즈로 복구

## 클래스 역할

### `Quiz`

퀴즈 하나를 표현합니다. 문제, 보기 4개, 정답 번호, 힌트를 보관하고 퀴즈 출력과 정답 확인을 담당합니다.

### `QuizGame`

퀴즈 풀기, 문제 수 선택, 랜덤 출제, 힌트 점수 차감, 문제 추가·삭제, 점수·히스토리 관리를 담당합니다.

### `Storage`

`state.json`의 읽기와 쓰기를 담당합니다. 기존 히스토리가 없는 저장 파일도 빈 기록으로 읽을 수 있습니다.

## 파일 구조

```text
mission2_quiz/
├── main.py
├── quiz.py
├── game.py
├── storage.py
├── test_quiz.py
├── test_storage.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
        ├── menu.png
        ├── play.png
        ├── add_quiz.png
        ├── score.png
        └── git_log.png
```

## 데이터 파일 설명

`state.json`은 프로젝트 루트에 저장됩니다.

```json
{
    "quizzes": [
        {
            "question": "파이썬에서 화면에 글자를 출력할 때 사용하는 함수는?",
            "choices": ["input()", "print()", "write()", "display()"],
            "answer": 2,
            "hint": "화면에 결과를 보여주는 함수입니다."
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

- `quizzes`: 등록된 퀴즈 목록
- `question`: 문제 내용
- `choices`: 4개의 선택지
- `answer`: 정답 번호
- `hint`: 힌트 문장
- `best_score`: 최고 점수
- `history`: 풀이 날짜·시간, 문제 수, 점수 기록

## 테스트

- `python test_quiz.py`: 퀴즈 정답 판정과 기본 문제 테스트
- `python test_storage.py`: 힌트와 점수 기록을 포함한 JSON 저장·복원 테스트

## Git 실습 기록

- 기능별 의미 있는 커밋 작성
- `feature/add-quiz` 브랜치에서 퀴즈 추가 기능 개발
- 기능 브랜치를 `main`에 병합
- GitHub에 `push`
- 별도 폴더에 `clone`
- 복제본에서 README 수정 후 `push`
- 원본 폴더에서 `pull`

## 실행 화면

- [메뉴 화면](docs/screenshots/menu.png)
- [퀴즈 풀이 결과](docs/screenshots/play.png)
- [퀴즈 추가 및 목록](docs/screenshots/add_quiz.png)
- [최고 점수](docs/screenshots/score.png)
- [Git 커밋 이력](docs/screenshots/git_log.png)

## 개선할 수 있는 점

- 문제별 난이도 추가
- 사용자별 점수 저장
- JSON 대신 데이터베이스 사용
