#!/usr/bin/python3
'''This module receives and formats json data from REST API
'''
import json
import requests
import sys

if __name__ == "__main__":
    url_1 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    response_1 = requests.get(url_1)
    users = response_1.json()
    EMPLOYEE_NAME = users.get("name")

    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': sys.argv[1]}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        todos = response.json()

    # Iterate through entire todos list
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for i in todos:
        if isinstance(i, dict):
            TOTAL_NUMBER_OF_TASKS += 1
        if i.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(i.get("title"))
    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
                ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for i in TASK_TITLE:
        print('\t ' + i)
