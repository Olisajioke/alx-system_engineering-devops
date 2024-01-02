#!/usr/bin/python3
"""A Python script that gets data from an API and converts it to JSON."""

import csv
import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    response = requests.get(user_url)
    USERNAME = response.json().get('username')
    task_url = user_url + '/todos'
    response = requests.get(task_url)
    tasks = response.json()

    dict_file = [{USER_ID: []}]
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_file[0][USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME})

    with open('{}.json'.format(USER_ID), 'w') as file_1:
        json.dump(dict_file, file_1)
