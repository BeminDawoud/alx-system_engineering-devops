#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {'User-Agent': 'MyRedditApp/0.1 by Bemin'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            if 'application/json' in response.headers.get('Content-Type', ''):
                data = response.json().get('data', {})
                children = data.get('children', [])
                for post in children:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
