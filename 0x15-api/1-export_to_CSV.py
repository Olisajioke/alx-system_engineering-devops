#!/usr/bin/python3
"""A python script that exports API data to CSV"""

import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    my_requests = requests.get(url_user)
    user = my_requests.json().get('username')
    task = url_user + '/todos'
    my_requests = requests.get(task)
    my_tasks = my_requests.json()

    with open('{}.csv'.format(user), 'w') as my_csv:
        for task in my_tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            my_csv.write('"{}","{}","{}","{}"\n'.format(
                user, user, completed, title_task))
