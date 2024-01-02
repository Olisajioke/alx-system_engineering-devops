#!/usr/bin/python3
'''A python script that gathers employee data from API'''

import requests
import sys
import re

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            em_id = int(sys.argv[1])
            rq = requests.get('{}/users/{}'.format(REST_API, em_id)).json()
            e_t_r = requests.get('{}/todos'.format(REST_API)).json()
            em_name = rq.get('name')
            em_task = list(filter(lambda x: x.get('userId') == em_id, e_t_r))
            tsk_don = list(filter(lambda x: x.get('completed'), em_task))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    em_name,
                    len(tsk_don),
                    len(em_task)
                )
            )
            if len(tsk_don) > 0:
                for task in tsk_don:
                    print('\t {}'.format(task.get('title')))
