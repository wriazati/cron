# Cron Expression Parser

This is a command-line application for parsing cron strings and expanding each field to show the times at which it will run. The goal of this project is to create a custom cron parser without using existing cron parser libraries to assess our ability to implement the logic ourselves.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Input Format](#input-format)
- [Output Format](#output-format)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this project, you can clone the repository and set up your development environment. Ensure you have your favorite programming language and tools installed.

```bash
git clone <repository_url>
cd cron-expression-parser

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Check
poetry --version

# Install venv
poetry install
```

## Usage

After setting up your development environment, you can run the application with the following command:

```bash
poetry run python main.py --cron '*/15 0 1,15 * 1-5 /usr/bin/find'
```

## Input Format

The input cron string should be passed as a single argument when running the program. The cron string follows the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

For example:

```
*/15 0 1,15 * 1-5 /usr/bin/find
```

## Output Format

The output of the program is formatted as a table with the field name taking the first 14 columns, followed by the times as a space-separated list. The output will look like this:

```
minute         0 15 30 45
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find
```

## Development

During development, please consider the following guidelines:
- Good luck

## Contributing

This project is a part of a coding exercise and does not currently accept contributions. However, feel free to fork the repository and extend it for your own use or educational purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
