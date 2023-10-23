#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import requests
import sys
import csv
import json


def fetchdata(employeeid):
    """ do json file from aspi"""
    if employeeid is None:
        return

    baseurl = f'https://jsonplaceholder.typicode.com/todos?userId={employeeid}'
    usersurl = f'https://jsonplaceholder.typicode.com/users/{employeeid}'
    user_rep = requests.get(usersurl)
    user_data = user_rep.json()
    if user_rep.status_code != 200:
        return

    base_rep = requests.get(baseurl)
    base_data = base_rep.json()
    tott = [task for task in base_data]
    username = user_data['username']
    userid = user_data['id']

    result = {}
    result[str(userid)] = []
    for task in tott:
        result[str(userid)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    # Now, let's save the data to a JSON file
    filename = f'{userid}.json'

    with open(filename, 'w') as jsonfile:
        json.dump(result, jsonfile)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    fetchdata(sys.argv[1])
