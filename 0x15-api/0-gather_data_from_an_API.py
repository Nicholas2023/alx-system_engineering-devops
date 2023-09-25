#!/usr/bin/python3
"""
Returns information about TODO list progress by employee id
"""

import requests
from sys import argv
from typing import List, Dict, Any, Union


def get_employee_todo_progress(employee_id: int) -> None:
    # Fetch TO-DO list data
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    data = requests.get(todo_url).json()

    # Fetch user data
    user_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(user_url).json()

    # Find the user by employee ID
    user: Dict[str, Union[int, str]] = \
        [i for i in users if i.get('id') == employee_id][0]

    # Filter tasks for the specified employee
    tasks: List[Dict[str, Any]] = \
        [i for i in data if i.get('userId') == employee_id]

    # Filter completed tasks
    completed_tasks: List[Dict[str, Any]] = \
        [i for i in tasks if i.get('completed') is True]

    # Print progress information
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer as the employee ID")
