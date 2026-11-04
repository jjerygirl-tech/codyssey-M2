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
5. 프로그램 종료

입력 검증 기능도 포함되어 있습니다.

- 빈 입력 처리
- 숫자가 아닌 입력 처리
- 허용 범위를 벗어난 숫자 처리
- `Ctrl+C`와 `EOFError` 안전 종료
- JSON 파일 손상 시 기본 퀴즈로 복구

## 클래스 역할

### `Quiz`

퀴즈 하나를 표현합니다.

- 문제, 보기 4개, 정답 번호 보관
- 퀴즈 출력
- 정답 확인
- JSON 저장용 딕셔너리 변환

### `QuizGame`

게임 전체를 관리합니다.

- 퀴즈 목록과 최고 점수 관리
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 보기
- 점수 확인
- 저장 기능 호출

### `Storage`

`state.json` 파일의 읽기와 쓰기를 담당합니다.

- 저장 파일 읽기
- 퀴즈와 최고 점수 저장
- 파일이 없을 때 기본 데이터 사용
- JSON이 손상되었을 때 기본 데이터로 초기화

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

`state.json`은 프로젝트 루트에 저장됩니다. 프로그램을 종료한 뒤 다시 실행해도 등록한 퀴즈와 최고 점수가 유지됩니다.

예시 구조:

```json
{
    "quizzes": [
        {
            "question": "파이썬에서 화면에 글자를 출력할 때 사용하는 함수는?",
            "choices": [
                "input()",
                "print()",
                "write()",
                "display()"
            ],
            "answer": 2
        }
    ],
    "best_score": 5
}
```

- `quizzes`: 등록된 퀴즈 목록
- `question`: 문제 내용
- `choices`: 4개의 선택지
- `answer`: 정답 번호
- `best_score`: 최고 정답 수

## 테스트 결과

- `python test_quiz.py` 통과
- `python test_storage.py` 통과
- 퀴즈 추가 후 재실행했을 때 데이터 복원 확인
- 잘못된 입력과 `Ctrl+C` 안전 종료 확인

## Git 실습 기록

기능별로 의미 있는 커밋을 만들었습니다.

- `main` 브랜치에서 기본 구조와 저장 기능 개발
- `feature/add-quiz` 브랜치에서 퀴즈 추가 기능 개발
- 기능 브랜치를 `main`에 병합
- GitHub에 `push`
- 별도 폴더에 `clone`
- 복제본에서 README 수정 후 `push`
- 원본 폴더에서 `pull`

주요 사용 명령어:

```text
git init
git add
git commit
git push
git pull
git checkout
git clone
```

## 실행 화면

실제 실행 결과는 다음 캡처에서 확인할 수 있습니다.

- [메뉴 화면](docs/screenshots/menu.png)
- [퀴즈 풀이 결과](docs/screenshots/play.png)
- [퀴즈 추가 및 목록](docs/screenshots/add_quiz.png)
- [최고 점수](docs/screenshots/score.png)
- [Git 커밋 이력](docs/screenshots/git_log.png)

## 개선할 수 있는 점

- 문제를 랜덤한 순서로 출제하기
- 퀴즈 삭제 기능 추가하기
- 퀴즈 풀이 기록을 날짜와 함께 저장하기
- 힌트 기능 추가하기
