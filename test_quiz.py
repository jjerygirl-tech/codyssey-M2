from quiz import Quiz, create_default_quizzes


def test_quiz_answer():
    quiz = Quiz(
        "파이썬에서 출력 함수는?",
        ["input()", "print()", "for", "if"],
        2,
    )

    assert quiz.is_correct(2)
    assert not quiz.is_correct(1)


def test_default_quizzes():
    quizzes = create_default_quizzes()

    assert len(quizzes) >= 5
    assert all(len(quiz.choices) == 4 for quiz in quizzes)
    assert all(1 <= quiz.answer <= 4 for quiz in quizzes)


if __name__ == "__main__":
    test_quiz_answer()
    test_default_quizzes()
    print("모든 테스트를 통과했습니다.")