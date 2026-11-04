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
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "5":
            print("프로그램을 종료합니다.")
            break
        elif choice in ["1", "2", "3", "4"]:
            print("이 기능은 다음 단계에서 구현합니다.")
        else:
            print("1부터 5 사이의 번호를 입력하세요.")


if __name__ == "__main__":
    main()