import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def load_guitars_from_file(filename):
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars_to_file(guitars, filename):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    guitars = load_guitars_from_file("guitars.csv")
    for guitar in guitars:
        print(guitar)

    # Ask user for new guitars
    while True:
        name = input("Enter guitar name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    # Save guitars to file
    save_guitars_to_file(guitars, "guitars.csv")


if __name__ == '__main__':
    main()