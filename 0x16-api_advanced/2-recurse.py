#!/usr/bin/python3
'''
    returns a list containing the titles of all hot articles for a given subreddit.
'''
import requests
import sys


def recurse(subreddit, params={}, hot_list=[]):
    '''returns a list containing the titles of all hot articles.'''
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'MyRedditApp/0.1 by Bemin'}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        data = response.json().get("data")
        if data is None:
            return hot_list
        for post in data.get("children", []):
            hot_list.append(post.get("data", {}).get("title"))
        after = data.get("after") 
        if after:
            params['after'] = after
            return recurse(subreddit, params=params, hot_list=hot_list)
        return hot_list
    except Exception:
        return None

if __name__ == '__main__':
    result = recurse(sys.argv[1])
    for res in result:
        print(res)

