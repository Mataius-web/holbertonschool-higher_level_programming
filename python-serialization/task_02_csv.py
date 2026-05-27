#!/usr/bin/env python3
"""Module to convert CSV data into JSON format"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file data to JSON format"""

    try:
        # Read CSV file
        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Write JSON file
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
