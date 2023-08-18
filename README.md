# Checkmate

Checkmate is a simple Python script that helps you generate todo lists in a file system hierarchy using Markdown files. It provides a convenient way to create and manage your daily todo lists in a structured format.

## Features

- Generates a markdown file for each day over a specified timespan.
- File system hierarchy with top-level directories as years, subdirectories as months, and text files in the format `DD.md` for each day.
- Each markdown file contains a header with the date in the format `# YYYY-MM-DD`.
- Command-line options to show unfinished tasks across the specified timespan.

## Usage

1. Install Python (if not already installed).
2. Clone the Checkmate repository.
3. Navigate to the repository directory.
4. Run the following command to generate todo files for a specified number of days:

```
python checkmate.py <number_of_days>
```

Replace `<number_of_days>` with the desired number of days.

5. (Optional) To display unfinished tasks across the specified timespan, use the `--show-unfinished` flag:

```
python checkmate.py <number_of_days> --show-unfinished
```

This will show a list of dates and corresponding unfinished tasks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

