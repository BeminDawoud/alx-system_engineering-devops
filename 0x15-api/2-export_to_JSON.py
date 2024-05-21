#!/usr/bin/python3
"""
Get tasks for user in a json file
"""
import json
import requests
import sys


if __name__ == "__main__":

    id = sys.argv[1]
    user_p = {"id": id}
    task_p = {"userId": id}
    user_url = "https://jsonplaceholder.typicode.com/users"
    task_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url, params=user_p).json()

    user_name = user[0]["username"]

    tasks = requests.get(task_url, params=task_p).json()

    task_list = []

    for task in tasks:
        task_list.append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name,
            }
        )
    task_dict = {f"{id}": task_list}
    with open(f"{id}.json", "w") as file:
        json.dump(task_dict, file)
