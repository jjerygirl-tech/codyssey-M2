from game import QuizGame


def show_menu():
    print("\n" + "=" * 40)
    print("        파이썬 기초 퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def main():
    game = QuizGame()

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            game.play_quiz()
        elif choice == "2":
            game.add_quiz()
        elif choice == "3":
            game.show_quiz_list()
        elif choice == "4":
            game.show_score()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("1부터 5 사이의 번호를 입력하세요.")


if __name__ == "__main__":
    main()