def main():
    score = None

    while True:
        print("Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").lower()

        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            print_result(score)
        elif choice == "s":
            show_stars(score)
        elif choice == "q":
            print("Farewell, see you again!")
            break
        else:
            print("Invalid choice, please try again.")


def get_valid_score():
    while True:
        score = input("Enter score (0-100): ")
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                return score
        print("Invalid score, please try again.")


def print_result(score):
    if score is None:
        print("You have not entered any score.")
    else:
        result = determine_status(score)
        print(f"Score: {score}, Result: {result}")


def show_stars(score):
    if score is None:
        print("You have not entered any score.")
    else:
        stars = "*" * score
        print(stars)


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
