#!/usr/bin/python3
"""A module contains the function top_ten"""

import requests
from sys import argv
import json


def top_ten(subreddit):
    '''A function that returns the top ten posts for a given subreddit'''
    user_agent = {'User-Agent': 'Bright'}

    url = requests.get(
        'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit),
        headers=user_agent
    )

    # Check if the response is successful (status code 200)
    if url.status_code == 200:
        try:
            data = url.json()
            for post in data.get('data', {}).get('children', []):
                print(post.get('data', {}).get('title'))
        except json.decoder.JSONDecodeError:
            print("Invalid JSON in the response.")
    else:
        print("Failed to retrieve data. Status code: {}"
              .format(url.status_code))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <subreddit>")
        exit(1)

    top_ten(argv[1])
