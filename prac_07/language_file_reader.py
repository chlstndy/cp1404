import csv
from prac_07.programming_language import ProgrammingLanguage


def read_languages(filename):
    """Read file of programming language details and return a list of ProgrammingLanguage objects."""
    languages = []

    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header line

        for row in csv_reader:
            name, typing, reflection, pointer_arithmetic, year = row
            reflection = reflection == "Yes"
            pointer_arithmetic = pointer_arithmetic == "Yes"
            year = int(year)
            language = ProgrammingLanguage(name, typing, reflection, pointer_arithmetic, year)
            languages.append(language)

    return languages


def display_languages(languages):
    """Display the details of programming languages."""
    for language in languages:
        print(language)


def main():
    """Read programming language details from file and display them."""
    filename = "languages.csv"
    languages = read_languages(filename)
    display_languages(languages)


if __name__ == "__main__":
    main()
