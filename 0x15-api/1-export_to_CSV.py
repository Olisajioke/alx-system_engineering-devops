#!/usr/bin/python3
""" A python script that exports api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + user
    response = requests.get(url)
    user_name = response.json().get('username')
    task = url + '/todos'
    response = requests.get(task)
    tasks = response.json()

    with open('{}.csv'.format(user), 'w') as myfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            myfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
