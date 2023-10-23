#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests
import sys


def fetchdata():
    """ do json file from aspi"""
    usersurl = 'https://jsonplaceholder.typicode.com/users/'
    user_rep = requests.get(usersurl)
    user_data = user_rep.json()
    if user_rep.status_code != 200:
        return
    totalresult = {}
    for user in user_data:
        ba = f'https://jsonplaceholder.typicode.com/todos?userId=\
        {user.get("id")}'
        base_rep = requests.get(ba)
        base_data = base_rep.json()
        tott = [task for task in base_data]
        username = user['username']
        userid = user['id']
        result = {}
        totalresult[str(userid)] = []
        result[str(userid)] = []
        for task in tott:
            result[str(userid)].append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
                })
        totalresult[str(userid)].append(result[str(userid)])
    # Now, let's save the data to a JSON file
    filename = 'todo_all_employees.json'
    with open(filename, 'a') as jsonfile:
        json.dump(totalresult, jsonfile)


if __name__ == '__main__':
    fetchdata()
