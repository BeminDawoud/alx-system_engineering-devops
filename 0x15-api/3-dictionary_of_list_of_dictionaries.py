#!/usr/bin/python3
"""
Get tasks for user
"""
import json
import requests


if __name__ == "__main__":

    all_employees_dict = {}
    user_url = "https://jsonplaceholder.typicode.com/users"
    task_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(user_url).json()
    tasks = requests.get(task_url).json()

    for user in users:
        user_list = []
        for task in tasks:
            if user["id"] == task["userID"]:
                task_dict = {}
                task_dict["task"] = task.get("title")
                task_dict["completed"] = task.get("completed")
                task_dict["username"] = user.get("username")
                user_list.append(task_dict)
        all_employees_dict[user["id"]] = user_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_employees_dict, file)
