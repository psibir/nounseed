import csv
import random
from pathlib import Path

STORED_NOUNS_FILE = "storednouns.csv"
CSV_FILE = "nounlist.csv"


class NounSeeder:
    def __init__(self, nouns):
        self.nouns = nouns

    @classmethod
    def load_nouns(cls, filename):
        csv_file = Path(filename)
        with csv_file.open('r') as csvfile:
            reader = csv.reader(csvfile)
            nouns = [row[0] for row in reader]
        return cls(nouns)

    def generate_project_ideas(self, num_ideas):
        if len(self.nouns) < 2:
            raise ValueError("There are not enough nouns to generate project ideas.")

        project_ideas = []
        for _ in range(num_ideas):
            noun1, noun2 = random.sample(self.nouns, 2)
            project_ideas.append(f"{noun1}{noun2}")

        return project_ideas


class ProjectIdeasManager:
    def __init__(self, ideas):
        self.ideas = ideas

    def select_ideas(self, user_input=input):
        while True:
            choices = user_input("Enter the numbers of the project ideas you want to store (comma-separated, e.g., 1,3,5), or enter 'view' to see stored ideas, or 'r' to remix the chosen nouns, or 't' to try again: ")

            if choices.lower() == 'view':
                return choices.lower()
            elif choices.lower() == 'r':
                return choices.lower()
            elif choices.lower() == 't':
                return choices.lower()

            choices = [int(choice.strip()) for choice in choices.split(',') if choice.strip().isdigit()]

            if not choices:
                print("No choices provided. Exiting the program.")
                raise SystemExit

            if any(choice not in range(1, len(self.ideas) + 1) for choice in choices):
                print("Invalid choices. Please enter valid numbers.")
                raise SystemExit

            return choices

    @staticmethod
    def remix_ideas(ideas):
        return random.sample(ideas, len(ideas))

    def store_ideas(self, choices, writer=print):
        if choices == 'view':
            self.view_stored_ideas(writer)
            return
        elif choices == 'r':
            self.ideas = self.remix_ideas(self.ideas)
            writer("Remixed Project Ideas:")
            for i, idea in enumerate(self.ideas, start=1):
                writer(f"{i}. {idea}")
            return
        elif choices == 't':
            return 't'

        stored_nouns_file = Path(STORED_NOUNS_FILE)
        with stored_nouns_file.open('a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for choice in choices:
                selected_idea = self.ideas[choice - 1]
                csv_writer.writerow([selected_idea])
                writer(f"Idea '{selected_idea}' has been stored in '{STORED_NOUNS_FILE}'.")

    @staticmethod
    def view_stored_ideas(writer=print):
        stored_nouns_file = Path(STORED_NOUNS_FILE)
        if stored_nouns_file.exists():
            with stored_nouns_file.open('r') as csvfile:
                reader = csv.reader(csvfile)
                stored_ideas = list(reader)
                writer("Stored Project Ideas:")
                for i, idea in enumerate(stored_ideas, start=1):
                    writer(f"{i}. {idea[0]}")
        else:
            writer("No stored project ideas found.")


def main(args):
    seed = NounSeeder.load_nouns(CSV_FILE)
    ideas = seed.generate_project_ideas(args.num_ideas)
    ideas_manager = ProjectIdeasManager(ideas)

    while True:
        print("Generated Project Ideas:")
        for i, idea in enumerate(ideas_manager.ideas, start=1):
            print(f"{i}. {idea}")

        choices = ideas_manager.select_ideas()
        if choices == 't':
            continue

        ideas_manager.store_ideas(choices)

        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() != 'y':
            break

    print("Exiting the program.")


if __name__ == '__main__':
    import argparse

    CSV_FILE = 'nounlist.csv'
    STORED_NOUNS_FILE = 'storednouns.csv'

    parser = argparse.ArgumentParser(description="Generate and store project ideas.")
    parser.add_argument("-n", "--num-ideas", type=int, default=10, help="number of project ideas to generate")
    args = parser.parse_args()

    main(args)
