"""Utility functions for reading JSON files."""

import json


def read_json_data(file_path: str) -> dict:
    """Read and return data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: dict = json.load(file)

        return data
    except FileNotFoundError:
        print("Error: JSON file was not found.")
        return {}
    
    except json.JSONDecodeError:
        print("Error: The file does not contain valid JSON.")
        return {}
    

file_path: str = ("student_data.json")

student_data: dict = read_json_data(file_path=file_path)

if student_data:
    print(f"Name: {student_data['name']}")
    print(f"Goal: {student_data['goal']}")
    print(f"Daily study hours: {student_data['daily_study_hours']} hours")
    print(f"Skills: {student_data['skills']}")