import random


questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) def", "C) fun", "D) define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A) String", "B) Integer", "C) Boolean", "D) Float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) /* */"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output?",
        "options": ["A) display()", "B) output()", "C) print()", "D) show()"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to check a condition?",
        "options": ["A) check", "B) if", "C) condition", "D) when"],
        "answer": "B"
    }
]


def show_title():
    print("\n" + "=" * 50)
    print("              PYTHON QUIZ GAME")
    print("=" * 50)
    print("Test your Python knowledge!")
    print("=" * 50)


def play_quiz():
    score = 0

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    for number, item in enumerate(quiz_questions, start=1):
        print("\nQuestion", number, "of", len(quiz_questions))
        print("-" * 50)
        print(item["question"])

        for option in item["options"]:
            print(option)

        while True:
            answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input. Please enter A, B, C or D.")

        if answer == item["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer.")
            print("Correct answer is:", item["answer"])

        print("Current score:", score)

    return score


def show_result(score):
    total = len(questions)
    percentage = (score / total) * 100

    print("\n" + "=" * 50)
    print("                 GAME OVER")
    print("=" * 50)
    print("Final Score :", score, "/", total)
    print("Percentage  :", f"{percentage:.0f}%")

    if percentage == 100:
        print("Performance : Excellent!")
    elif percentage >= 80:
        print("Performance : Great job!")
    elif percentage >= 60:
        print("Performance : Good work!")
    elif percentage >= 40:
        print("Performance : Keep practicing!")
    else:
        print("Performance : Don't give up!")

    print("=" * 50)


def main():
    while True:
        show_title()

        print("\nInstructions:")
        print("1. There are 5 questions.")
        print("2. Choose A, B, C or D.")
        print("3. Each correct answer gives 1 point.")

        input("\nPress Enter to start...")

        score = play_quiz()
        show_result(score)

        choice = input("\nDo you want to play again? (Y/N): ").strip().upper()

        if choice != "Y":
            print("\nThank you for playing!")
            print("Keep learning Python!")
            break


if __name__ == "__main__":
    main()