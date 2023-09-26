#!/usr/bin/python3
"""
Returns information about TODO list progress by employee id
and exports it to a CSV file
"""

import csv
import requests
import sys
from sys import argv


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Fetch the TO-DO list data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = todos_response.json()

    # Fetch the user data
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    # Find the user by user ID
    user_id = int(argv[1])
    user = next((u for u in users_data if u['id'] == user_id), None)

    if user is None:
        print("User ID and Username: User not found.")
    else:
        # Filter tasks owned by the user
        user_tasks = [task for task in todos_data if task['userId'] == user_id]

        # Create and write to the CSV file
        csv_file_name = "{}.csv".format(user_id)

        # Write data to CSV file
        with open(csv_file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

            writer.writerow([
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ])

            for task in user_tasks:
                writer.writerow([
                    str(user_id),
                    user['username'],
                    str(task['completed']),
                    task['title']
                ])
    print("Data exported to {}".format(csv_file_name))
