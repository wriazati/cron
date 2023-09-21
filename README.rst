
# Build

This was developed on python 3.11.3. With poetry you can initialize the environment to download the necessary packages.
I also have sample output in an image in this directory.


# Enable env

source .venv/bin/activate

# Run tests

poetry run pytest

# Sample commands


PYTHONPATH='.' poetry run python main.py --data data/SciTec_code_problem_data.csv --sample

PYTHONPATH='.' poetry run python main.py --data data/SciTec_code_problem_data.csv --request 5

PYTHONPATH='.' poetry run python main.py --data data/SciTec_code_problem_data.csv --request 1532334000

PYTHONPATH='.' poetry run python main.py --data data/SciTec_code_problem_data.csv --request 1532334777

