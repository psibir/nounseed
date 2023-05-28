# NounSeed

NounSeed is a Python script that generates and manages project ideas based on a list of nouns. It allows you to select and store project ideas, view stored ideas, remix the chosen nouns, and try generating project ideas again.

## Prerequisites

- Python 3.x
- Required Python packages: `csv`, `random`, `pathlib`

## Usage

1. Make sure you have the required Python packages installed.
2. Place your list of nouns in a CSV file named `nounlist.csv`. Each noun should be listed in a separate row.
3. Run the `nounseed.py` script using the following command:

   ```
   python nounseed.py [-n NUM_IDEAS]
   ```

   Optional arguments:
   - `-n NUM_IDEAS`: Number of project ideas to generate (default is 10)

4. The script will display a list of generated project ideas with corresponding numbers.
5. Enter the numbers of the project ideas you want to store, separated by commas. Alternatively, you can enter:
   - `view` to see the stored project ideas
   - `r` to remix the chosen nouns and display the new project ideas
   - `t` to try generating project ideas again
6. If you selected project ideas to store, they will be stored in a CSV file named `storednouns.csv`.
7. After storing project ideas or viewing them, you will be prompted to try again. Enter `y` to generate project ideas again or `n` to exit the program.

## File Descriptions

- `nounseed.py`: The main script file that generates and manages project ideas.
- `nounlist.csv`: A CSV file containing the list of nouns used for generating project ideas.
- `storednouns.csv`: A CSV file where the stored project ideas are stored.

## Customization

- To modify the input noun list, update the `nounlist.csv` file with your desired nouns.
- To change the generated project ideas limit, use the `-n` or `--num-ideas` argument when running the script.
- To change the file names for the noun list and stored ideas, update the `CSV_FILE` and `STORED_NOUNS_FILE` variables in the script.

## License

This project is licensed under the [MIT License](LICENSE).