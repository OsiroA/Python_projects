# Word Count and Most Occurring Word

This Python script counts the number of words in a text file and identifies the most occurring word along with its frequency.

## Getting Started

1. Make sure you have Python 3 installed on your system.

2. Download or clone the Python script from this repository.

3. Place the script file in the same directory as the text file you want to analyze.

## Usage

1. Run the script using the following command:

   ```
   python word_count.py
   ```

2. You will be prompted to enter the name of the text file you want to read. Please provide the name without the file extension.

3. The script will read the contents of the specified text file and count the words.

4. It will then determine the most occurring word and display it along with the number of times it appears in the text.

## Example

Suppose we have a text file named `sample_text.txt` with the following content:

```
Hello world! This is a sample text file. It contains some words and repeated words.
```

Running the script and entering `sample_text` when prompted, the output will be:

```
The most occurring word is 'words' and it appears 2 times.
```

## Dependencies

This script utilizes the `collections.Counter` class from the Python standard library to count word occurrences.

## Limitations

- The script treats each word as a separate entity based on whitespace separation. Thus, words separated by punctuation or special characters are considered distinct.

- The script does not account for variations in letter casing. For example, "Hello" and "hello" would be treated as different words.

- In case of multiple words having the same maximum frequency, the script only reports the first word encountered during the sorting process.

## Contributing

Contributions to improve the script are welcome! If you encounter any issues, have suggestions, or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Please let me know if you need any further assistance!
