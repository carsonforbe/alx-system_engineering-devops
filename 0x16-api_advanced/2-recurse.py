#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list of hot article titles for a given subreddit. 
    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): The list to store the hot article titles. Defaults to None.
        after (str): The "after" parameter for pagination. Defaults to None.
    Returns:
        list: A list of hot article titles for the given subreddit, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/0.1"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            return hot_list

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 302:
        return None
    else:
        return None
