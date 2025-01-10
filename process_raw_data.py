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

def get_authors_names():
    """Query database for map"""
    pass


def get_relevant_data(data: list[str]) -> list[dict]:
    """Gets only the relevant columns."""
    relevant_data = []
    for row in data:
      relevant_data.append({
            "title": row["book_title"],
            "author_id": row["author_id"],
            "year": row["Year released"],
            "rating": row["Rating"],
            "ratings": row["ratings"]
      })
    return relevant_data


def filter_for_author_title_missing_data(data: list[dict]) -> list[dict]:
    """Check each row for valid data."""
    filtered_data = []
    for row in data:
        title = row["title"]
        author_id = row["author_id"]
        if title != '' and author_id != '':
            filtered_data.append(row)
    return filtered_data
            

def clean_title(data: list[dict]): #ADD TYPE
    for row in data:
        title = row["title"]
        if "(" in title:
            row["title"] = title.split('(')[0].strip()
    return data


def clean_author_id(data: list[dict]): #ADD TYPE
    for row in data:
        row["author_id"] = int(float(row["author_id"]))
    return data


def clean_year(data: list[dict]): #ADD TYPE
    for row in data:
        row["author_id"] = int(row["year"])
    return data


def clean_rating(data: list[dict]): #ADD TYPE
    for row in data:
        row["rating"] = float(row["rating"].replace(",", "."))
    return data
 

def clean_ratings(data: list[dict]): #ADD TYPE
    for row in data:
        row["ratings"] = int(row["ratings"].replace("`", ""))
    return data


# Create csv
def create_csv(data: list[dict], filename: str, folder: str='data') -> None:
    """Creates a csv."""
    with 



if __name__ == "__main__":
    # Initialise
    filename = get_cli_args()

    # Get csv data
    data = get_csv_data(filename)

    # Clean data
    data = get_relevant_data(data)
    data = filter_for_author_title_missing_data(data)
    data = clean_title(data)
    data = clean_author_id(data)
    data = clean_year(data)
    data = clean_rating(data)
    data = clean_ratings(data)



    for i in range(10):
        print(data[i])
    # Create csv