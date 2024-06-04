#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditApp/0.1 by Bemin'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            subs = response.json().get('data').get('subscribers')
            return subs
        else:
            return 0
    except Exception:
        return 0
