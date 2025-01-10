"""A script to process book data."""
from argparse import ArgumentParser
import csv 


# Initialise
def get_cli_args() -> str:
    """Gets cli filename argument."""
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename", required=True, type=str, 
                help="-f or --filename, must enter a csv file location.")
    args = parser.parse_args()
    return args.filename
    # Check if file exists, raise error


# Get data
def get_csv_data(file_name: str, folder: str='data') -> list[dict]:
    """Get the csv data from a specified file,
    return as a list of dictionaries."""
    with open(f'{folder}/{file_name}', mode='r', encoding="UTF-8") as csv_file:
        rows = csv.DictReader(csv_file)
        return [row for row in rows]


# Transform

def get_authors_names()


def check_title(data: list[dict]): #ADD TYPE
    pass


def check_author_name(data: list[dict]): #ADD TYPE
    pass


def check_year(data: list[dict]): #ADD TYPE
    pass


def check_rating(data: list[dict]): #ADD TYPE
    pass

def check_ratings(data: list[dict]): #ADD TYPE
    pass


def filter_for_errors(data: list[dict]) -> list[dict]:
    """Check each row for valid data."""
    pass


# Create csv
def create_csv(data: list[dict], filename: str, folder: str='data') -> None:
    """Creates a csv."""
    pass



if __name__ == "__main__":
    # Initialise
    filename = get_cli_args()

    # Get csv data
    csv_data = get_csv_data(filename)

    # Clean data

    # Create csv