import random


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_status(user_score)
    print(user_result)

    random_score = random.randint(0, 100)
    random_result = determine_status(random_score)
    print(f"Random score: {random_score}, result: {random_result}")


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
