# nounseed

![image](/nounseed_logo.png)

This is a Python script that generates and stores project ideas based on a list of nouns. The `NounSeeder` class is responsible for loading the nouns, generating project ideas, and storing them. The script utilizes the `csv` module and the `pathlib` module for file operations.

## Features

- **Loading Nouns**: The `NounSeeder` class provides a `load_nouns` method that loads a list of nouns from a CSV file. The CSV file should have one noun per line.

- **Generating Project Ideas**: The `NounSeeder` class has a `generate_project_ideas` method that generates project ideas by combining two randomly selected nouns from the loaded list. It ensures that there are at least two nouns available for generating ideas.

- **Selecting Project Ideas**: The `select_project_ideas` function allows the user to select project ideas from a given list. The user can input the numbers of the project ideas they want to store or enter 'view' to see the stored ideas.

- **Storing Project Ideas**: The `store_project_ideas` function stores the selected project ideas in a CSV file. The stored ideas are appended to the file, and each idea is stored on a separate line.

- **Viewing Stored Ideas**: The `view_stored_ideas` function displays the stored project ideas from the CSV file.

## Usage

1. Install the required dependencies (if not already installed). The script uses the built-in `csv` module and `pathlib` module, so no additional installation is necessary.

2. Prepare the noun list: Create a CSV file named `nounlist.csv` and populate it with one noun per line.

3. Run the script: Execute the `main.py` script using Python. You can provide an optional argument `-n` or `--num-ideas` to specify the number of project ideas to generate (default is 10).

   ```shell
   python main.py -n 10
   ```

4. Follow the prompts: The script will generate project ideas and display them with corresponding numbers. Enter the numbers of the project ideas you want to store (comma-separated) or enter 'view' to see the stored ideas.

5. View stored ideas: If you choose 'view', the script will display the stored project ideas from the `storednouns.csv` file.

6. Exit the program: Once you have made your selections, the script will exit.

## File Structure

- `main.py`: The main script that orchestrates the generation and storage of project ideas.
- `nounseed/`: A package directory containing the following modules:
  - `__init__.py`: An empty file that makes the `nounseed` directory a Python package.
  - `csv_utils.py`: A module containing utility functions for reading and writing CSV files.

## Configuration

The script uses the following configuration variables:

- `STORED_NOUNS_FILE`: The name of the CSV file where the selected project ideas will be stored.
- `CSV_FILE`: The name of the CSV file containing the list of nouns.

You can modify these variables in the script to customize the filenames or paths according to your requirements.

**Note:** Make sure to place the `main.py` script in the same directory as the `nounseed` package directory for the relative imports to work correctly.

## Dependencies

The script requires the following dependencies:

- Python 3.x: The script is written in Python and requires Python 3 or higher to run.
- `csv` module: The script utilizes the built-in `csv` module for reading and writing CSV files.
- `pathlib` module: The script uses the `pathlib` module for file operations and path manipulation.

No additional external

 libraries or packages are required.

## License

This script is released under the MIT License. You can find the full license text in the `LICENSE` file.

## Contributions

Contributions to the script are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any direct or indirect damage caused by using this script.
