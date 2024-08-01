#!/usr/bin/python3
'''This module receives and formats json data from REST API
It then exports user-specific data in JSON format
'''
import json
import requests
import sys

if __name__ == "__main__":
    # Create dictionary profile for all users
    users_data = {}

    # Reiterate through each individual user
    for i in range(1, 11):
        USER_ID = i
        url_1 = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
        response_1 = requests.get(url_1)
        user = response_1.json()
        USERNAME = user.get("username")

        # Retrieve tasks of user
        url = 'https://jsonplaceholder.typicode.com/todos'
        params = {'userId': USER_ID}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            todos = response.json()

        # Create empty dictionary
        data = {}

        # Populate dictionary with details of USER_ID
        data[f"{USER_ID}"] = [{
            "task": f"{i.get('title')}",
            "completed": i.get("completed"),
            "username": f"{USERNAME}"
        } for i in todos]

        # Add data to users dictionary
        users_data.update(data)

    # Create custom filename
    filename = f"todo_all_employees.json"

    # Write data of all users into json file
    with open(filename, 'w') as f:
        json.dump(users_data, f)
