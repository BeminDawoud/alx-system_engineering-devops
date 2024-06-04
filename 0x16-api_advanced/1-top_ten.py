#!/usr/bin/python3
'''
    prints the titles of the first 10 hot posts listed for a given subreddit.
'''
from sys import argv
import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 posts for a given subreddit.'''
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {'User-Agent': 'MyRedditApp/0.1 by Bemin'}
    response = requests.get(url, headers=headers).json()
    try:
        for post in response.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
