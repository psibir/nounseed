# nounseed

![logo](/nounseed_logo.png)

`nounseed` is a Python program that generates and stores project ideas based on randomly chosen nouns. It utilizes two classes, `NounSeeder` and `ProjectIdeasManager`, to handle the generation and management of project ideas.

## Usage

To use the `nounseed` program, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the `nounseed` repository from GitHub:

   ```shell
   git clone https://github.com/psibir/nounseed.git
   ```

3. Navigate to the cloned directory:

   ```shell
   cd nounseed
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the program with the desired number of project ideas to generate:

   ```shell
   python -m nounseed --num-ideas <number_of_ideas>
   ```

   Replace `<number_of_ideas>` with the desired number of project ideas to generate. If no number is provided, the program will generate 10 project ideas by default.

6. Follow the on-screen instructions to store project ideas, remix chosen nouns, generate new nouns, view stored ideas, or quit the program.

## Dependencies

The `nounseed` program has the following dependencies:

- Python 3.x
- `argparse` (standard library)
- `csv` (standard library)
- `random` (standard library)
- `pathlib` (standard library)

## Files

- `__main__.py`: This script contains the main functionality of the `nounseed` program. It generates and stores project ideas based on user input.
- `nounlist.csv`: This CSV file contains a list of nouns that are used to generate project ideas.
- `storednouns.csv`: This CSV file stores the project ideas that the user chooses to store during the program execution.

# License

See the [LICENSE](LICENSE)