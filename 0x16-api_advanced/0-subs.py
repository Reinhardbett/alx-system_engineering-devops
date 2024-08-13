#!/usr/bin/python3
''' This module queries the Reddit API and returns
number of subscribers for a given subreddit
'''
import json
import requests


def number_of_subscribers(subreddit):
    ''' Return the subscriber count of each subreddit
    If not valid, return 0.
    '''
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {
        'User-agent': 'Google Chrome Version 81.0.4044.129'
    }

    # Ensure we are not following redirects in GET request
    # Specify user-agent for granted access
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return (data.get("data").get("subscribers"))
    else:
        return (0)
