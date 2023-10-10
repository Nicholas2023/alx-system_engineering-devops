# Reddit API Tasks :wink:

This repository contains Python scripts to interact with the Reddit API. These scripts perform various tasks such as retrieving the number of subscribers, fetching the top posts, and recursively collecting hot articles for a given subreddit.

## Prerequisites

Before running the scripts, make sure you have Python installed on your system. You also need to install the `requests` library using the following command:

```bash
pip install requests
```

## Task 0: Number of Subscribers

The `0-subs.py` script allows you to find the total number of subscribers for a given subreddit.

### Usage

```bash
python 0-main.py subreddit_name
```

Replace `subreddit_name` with the name of the subreddit you want to query.

## Task 1: Top Ten Posts

The `1-top_ten.py` script fetches and prints the titles of the first 10 hot posts for a given subreddit.

### Usage

```bash
python 1-main.py subreddit_name
```

Replace `subreddit_name` with the name of the subreddit you want to query.

## Task 2: Recurse it!

The `2-recurse.py` script retrieves all hot articles for a given subreddit using recursion.

### Usage

```bash
python 2-main.py subreddit_name
```

Replace `subreddit_name` with the name of the subreddit you want to query.
