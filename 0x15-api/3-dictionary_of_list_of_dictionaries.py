#!/usr/bin/python3
"""A Python script that fetchess Rest API for todo lists of employees"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    my_users = response.json()

    dict_data = {}
    for user in my_users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url += '/todos/'
        response = requests.get(url)

        my_tasks = response.json()
        dict_data[USER_ID] = []
        for task in my_tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            dict_data[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
    with open('todo_all_employees.json', 'w') as file_2:
        json.dump(dict_data, file_2)
