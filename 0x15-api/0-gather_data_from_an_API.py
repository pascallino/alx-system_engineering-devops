#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetchdata(employeeid):
    """ Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
    """
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
    comt = [task for task in base_data if task['completed']]
    tott = [task for task in base_data]
    username = user_data['name']
    # Print the result
    print(f'Employee {username} is done with tasks({len(comt)}/{len(tott)}):')
    for task in comt:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    fetchdata(sys.argv[1])
