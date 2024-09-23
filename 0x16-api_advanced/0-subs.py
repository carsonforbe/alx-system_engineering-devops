#!/usr/bin/python3

"""
imports the requests module
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subsfor a given subrdt.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subs for the subreddit,or 0 if the subrdt invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Reddit subscriber count checker'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()#Raise exception for 4xx 5xx status codes
        data = response.json()
        return data['data']['subscribers']
    except (requests.exceptions.HTTPError, KeyError):
        return 0
