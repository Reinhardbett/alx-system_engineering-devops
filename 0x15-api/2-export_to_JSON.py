#!/usr/bin/python3
'''This module receives and formats json data from REST API
It then exports user-specific data in JSON format
'''
import json
import requests
import sys

if __name__ == "__main__":
    url_1 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    response_1 = requests.get(url_1)
    users = response_1.json()

    # Get username and user_id
    USER_ID = users.get("id")
    USERNAME = users.get("username")

    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': sys.argv[1]}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        todos = response.json()

    # Create and fill data dictionary
    data = {}

    # Initialize list for USER_ID
    if USER_ID not in data:
        data[f"{USER_ID}"] = []

    data[f"{USER_ID}"] = [{
        "task": f"{i.get('title')}",
        "completed": i.get("completed"),
        "username": f"{USERNAME}"
    } for i in todos]

    # Create filename
    filename = f"{USER_ID}.json"

    # Write data into json file
    with open(filename, 'w') as f:
        json.dump(data, f)
