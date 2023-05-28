# nounseed

![image](/nounseed_logo.png)

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

## File Structure

- `main.py`: The main script that orchestrates the generation and storage of project ideas.
- `nounseed/`: A package directory containing the following modules:
  - `__init__.py`: An empty file that makes the `nounseed` directory a Python package.
  - `csv_utils.py`: A module containing utility functions for reading and writing CSV files.

## Configuration

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

This script is released under the MIT License. You can find the full license text in the `LICENSE` file.

## Contributions

Contributions to the script are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any direct or indirect damage caused by using this script.