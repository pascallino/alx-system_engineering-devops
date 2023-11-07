#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API, parses
he title of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not)."""
import requests


def count_words(subreddit, word_list, allwords={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        allwords (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if allwords.get(word) is None:
                    allwords[word] = times
                else:
                    allwords[word] += times

    if after is None:
        if len(allwords) == 0:
            print("")
            return
        allwords = sorted(allwords.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in allwords:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, allwords, after, count)
