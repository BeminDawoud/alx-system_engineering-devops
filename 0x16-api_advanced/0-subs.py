#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/.json'
    headers = {'User-Agent': 'MyRedditApp/0.1 by YourUsername'}
    try:
        response = requests.get(url, headers=headers)
        children = response.json().get('data').get('children')
        subs = children[0].get("data").get("subreddit_subscribers")
        if subs:
            return children[0].get("data").get("subreddit_subscribers")
        else:
            return 0
    except Exception:
        return 0
