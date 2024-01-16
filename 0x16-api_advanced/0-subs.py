#!/usr/bin/python3
'''  Module that contains the function number_of_subscribers'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''A function that returns the number of subs for a subreddit'''
    user_agent = {'User-Agent': 'Olisa/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json().get('data')
        subscribers = data.get('subscribers') if data else 0

        return subscribers
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    if len(argv) == 2:
        subreddit_name = argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(f"The subreddit '{subreddit_name}' "
              f"has {subscribers_count} subscribers.")
    else:
        print("Usage: python script.py <subreddit_name>")
