#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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
    tott = [task for task in base_data]
    username = user_data['name']
    userid = user_data['id']
    # Print the result
    dict = {}
    list = []
    for task in tott:
        dict['USER_ID'] = userid
        dict['USERNAME'] = username
        dict['TASK_COMPLETED_STATUS'] = task.get('completed')
        dict['TASK_TITLE'] = task.get("title")
        list.append(dict)
        dict = {}
    # Now, let's save the data to a CSV file
    filename = f'{userid}.csv'

    with open("{}.csv".format(userid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userid, username, t.get("completed"), t.get("title")]
                ) for t in tott]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    fetchdata(sys.argv[1])
