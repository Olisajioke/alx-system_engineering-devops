#!/usr/bin/env python3
""" fUNCTION THAT RETURNS SUBSCRIBERS"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: Number of subscribers for the subreddit. Returns 0
    """

    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        headers = {'User-Agent': 'Paul'}

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
