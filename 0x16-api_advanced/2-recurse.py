#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a
list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a
    list of titles of all hot articles for the given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles
                         (used for recursion).
        after (str): Identifier for pagination (used for recursion).
    Returns:
        list: A list containing titles of all hot articles for
              the subreddit. Returns None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "custom-agent"}
    params = {"after": after} if after else None
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
