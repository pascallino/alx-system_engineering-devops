#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests
import sys


def fetchdata():
    """ do json file from aspi"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    totalresult = {}
    for user in users:
        tott = requests.get(url + "todos",
                            params={"userId": user.get("id")}).json()
        username = user['username']
        userid = user['id']
        result = []
        for task in tott:
            result.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": username
                })
        totalresult[str(userid)] = result
    # Now, let's save the data to a JSON file
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(totalresult, jsonfile)


if __name__ == '__main__':
    fetchdata()
