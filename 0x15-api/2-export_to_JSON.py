#!/usr/bin/python3
"""
Returns information about TODO list progress by employee ID and
and exports it to JSON
"""

import json
import requests
import sys
from sys import argv


if __name__ == "__main__":
    # Fetch the TO-DO list data
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()

    # Fetch the user data
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()

    # Extract user ID from command line
    user = [i for i in users if i.get('id') == int(argv[1])][0]
    tasks = [i for i in data if i.get('userId') == int(argv[1])]
    with open(argv[1] + '.json', 'w', newline='') as f:
        expo = {argv[1]: []}
        lis = expo.get(argv[1])
        for task in tasks:
            lis.append({"task": task.get('title'), "completed": task.
                       get('completed'), "username": user.get('username')})
        f.write(json.dumps(expo))
        f.close()
