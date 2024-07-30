#!/usr/bin/python3
'''This module creates a csv file for data retrieved from REST API
'''
import json
import requests
import sys
import csv

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url_1 = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_1 = requests.get(url_1)
    users = response_1.json()
    USERNAME = users.get("username")

    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': USER_ID}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        todos = response.json()

    filename = f"{USER_ID}.csv"
    with open(filename, 'w', newline='') as f:
        fieldnames = [
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
        write_csv = csv.DictWriter(
            f,
            fieldnames,
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        for i in todos:
            TASK_COMPLETED_STATUS = i.get("completed")
            TASK_TITLE = i.get("title")
            row = {
                "USER_ID": USER_ID,
                "USERNAME": USERNAME,
                "TASK_COMPLETED_STATUS": TASK_COMPLETED_STATUS,
                "TASK_TITLE": TASK_TITLE
            }
            write_csv.writerow(row)
