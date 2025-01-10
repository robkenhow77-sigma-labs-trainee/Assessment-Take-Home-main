"""A script to process book data."""
from argparse import ArgumentParser
import csv
import sqlite3


# Initialise
def get_cli_args() -> str:
    """Gets cli filename argument."""
    parser = ArgumentParser()
    parser.add_argument("filename",type=str,
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
        return list(rows)


def get_authors_names(filename:str="authors.db", folder:str="data") -> list[tuple]:
    """Query database for author_id and author_name"""
    conn = sqlite3.connect(f'{folder}/{filename}')
    cur = conn.cursor()
    cur.execute("SELECT * FROM author"  )
    authors_list = cur.fetchall()
    cur.close()
    conn.close()
    return authors_list


# Transform
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


def clean_title(data: list[dict]) -> list[dict]:
    """Cleans the book title to the appropriate format."""
    for row in data:
        title = row["title"]
        if "(" in title:
            title = title.split('(')[0].strip()
        row["title"] = title.replace('"', '')
    return data


def clean_author_id(data: list[dict]) -> list[dict]:
    """Cleans the author_id to the appropriate format."""
    for row in data:
        row["author_id"] = int(float(row["author_id"]))
    return data


def clean_year(data: list[dict]) -> list[dict]:
    """Cleans the book year to the appropriate format."""
    for row in data:
        row["year"] = int(row["year"])
    return data


def clean_rating(data: list[dict]) -> list[dict]:
    """Cleans the book rating to the appropriate format."""
    for row in data:
        row["rating"] = float(row["rating"].replace(",", "."))
    return data


def clean_ratings(data: list[dict]) -> list[dict]:
    """Cleans the book ratings to the appropriate format."""
    for row in data:
        row["ratings"] = int(row["ratings"].replace("`", ""))
    return data


def map_author_id(data: list[dict], authors_and_id: list[tuple]) -> list[dict]:
    """Creates a mapping dicitonary in the form -> id: name
    Then maps the author_id to author_name.
    Adds author_name key and removes authour_id """
    mapping = {str(author[0]): author[1] for author in authors_and_id}
    for row in data:
        author_id = row["author_id"]
        author_name = mapping[str(author_id)]
        row["author_name"] = author_name
        row.pop("author_id")
    return data


def order_rows_by_rating(data:list[dict]) -> list[dict]:
    """Orders the rows based on rating."""
    return sorted(data, key=lambda row: row['rating'], reverse=True)


# Create csv
def create_csv(data: list[dict], filename: str='PROCESSED_DATA.csv') -> None:
    """Creates a csv."""
    with open(filename, mode='w', newline='', encoding="UTF-8") as new_csv:
        writer = csv.writer(new_csv)
        # Write Header
        writer.writerow(["title", "author_name", "year", "rating", "ratings"])
        # Write rows
        for row in data:
            values = [row["title"], row["author_name"], row["year"], row["rating"], row["ratings"]]
            writer.writerow(values)


if __name__ == "__main__":
    # Initialise
    file = get_cli_args()

    # Get csv and author data
    csv_data = get_csv_data(file)
    authors = get_authors_names()

    # Clean data
    cleaning_data = get_relevant_data(csv_data)
    cleaning_data = filter_for_author_title_missing_data(cleaning_data)
    cleaning_data = clean_title(cleaning_data)
    cleaning_data = clean_author_id(cleaning_data)
    cleaning_data = clean_year(cleaning_data)
    cleaning_data = clean_rating(cleaning_data)
    cleaning_data = clean_ratings(cleaning_data)
    cleaning_data = map_author_id(cleaning_data, authors)
    clean_data = order_rows_by_rating(cleaning_data)

    # Create csv
    create_csv(clean_data)


    # with open()
