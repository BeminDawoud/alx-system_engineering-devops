#!/usr/bin/python3
"""
Get tasks for user
"""
import requests
import sys


if __name__ == "__main__":

    id = sys.argv[1]
    user_p = {"id": id}
    task_p = {"userId": id}
    user_url = "https://jsonplaceholder.typicode.com/users"
    task_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url, params=user_p).json()

    user_name = user[0]["name"]

    tasks = requests.get(task_url, params=task_p).json()

    task_list = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    for task in tasks:
        if task["completed"] is True:
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
            task_list.append(task["title"])

    print(
        f"Employee {user_name} is done with tasks"
        + f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )
    for task in task_list:
        print(f"\t {task}")
