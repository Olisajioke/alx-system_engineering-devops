#!/usr/bin/python3
"""Python script to retrieve data from an API and convert to JSON"""

import csv
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    my_request = requests.get(user_url)
    """Documentation"""
    username = my_request.json().get('username')
    """Documentation"""
    task_url = user_url + '/todos'
    my_request = requests.get(task_url)
    my_tasks = my_request.json()

    dict_file = {user_id: []}
    for task in my_tasks:
        completed_status = task.get('completed')
        task_title = task.get('title')
        dict_file[user_id].append({
            "task": task_title,
            "completed": completed_status,
            "username": username
        })
    """print(dict_file)"""
    with open('{}.json'.format(user_id), 'w') as file_1:
        json.dump(dict_file, file_1)
