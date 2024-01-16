#!/usr/bin/python3
'''Module that contains the function number_of_subscribers'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''A function that returns the number of subs for a subreddit'''
    user_agent = {'User-Agent': 'Bright'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json().get('data')
        subscribers = data.get('subscribers') if data else 0

        return subscribers
    except requests.RequestException as e:
        print("Error: {}".format(e))
        return 0


if __name__ == "__main__":
    if len(argv) == 2:
        subreddit_name = argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print("The subreddit '{}' has {} "
              "subscribers.".format(subreddit_name, subscribers_count))
    else:
        print("Usage: python script.py <subreddit_name>")
