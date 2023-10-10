#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse titles of hot articles,
and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API and prints a
    sorted count of given keywords.
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): Identifier for pagination (used for recursion).
        count_dict (dict): Dictionary to store the count of keywords
                           (used for recursion).
    """
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "custom-agent"}
    params = {"after": after} if after else None
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    count_dict[word.lower()] = count_dict.get(word.lower(),
                                                              0) + 1
        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1],
                                                                      x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("None")
