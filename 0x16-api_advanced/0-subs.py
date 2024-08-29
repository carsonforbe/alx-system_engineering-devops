#!/usr/bin/python3

"""
importing requests module
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-agent": "Custom"}
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
