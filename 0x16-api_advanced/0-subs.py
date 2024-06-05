#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    headers = {'User-Agent': 'MyRedditApp/0.1 by Bemin'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            subs = data.get('subscribers')
            if subs is not None:
                return subs
            else:
                return 0
        else:
            return 0
    except Exception:
        return 0
