#!/usr/bin/python3
"""
Get tasks for user in a csv file
"""
import csv
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
        task_list.append([id, user_name, task["completed"], task["title"]])

    with open(f"{id}.csv", "w") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in task_list:
            csv_writer.writerow(task)
