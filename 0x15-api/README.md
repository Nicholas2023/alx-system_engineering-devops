# Employee Task Management API Integration :smile:

This project involves interacting with an Employee Task Management REST API to perform various tasks related to employee tasks and data export. The tasks include gathering data for a specific employee, exporting their task information to CSV and JSON files, and creating a dictionary of tasks for all employees.

## Task Descriptions

### Task 0: Gather Data from an API
- **File:** `0-gather_data_from_an_API.py`
- **Usage:** `python3 0-gather_data_from_an_API.py <employee_id>`
- This script retrieves information about a specific employee from the API and lists the tasks completed by that employee.

### Task 1: Export to CSV
- **File:** `1-export_to_CSV.py`
- **Usage:** `python3 1-export_to_CSV.py <employee_id>`
- This script exports the task data of a specific employee to a CSV file.

### Task 2: Export to JSON
- **File:** `2-export_to_JSON.py`
- **Usage:** `python3 2-export_to_JSON.py <employee_id>`
- This script exports the task data of a specific employee to a JSON file.

### Task 3: Dictionary of List of Dictionaries
- **File:** `3-dictionary_of_list_of_dictionaries.py`
- This script fetches task data for all employees and creates a dictionary containing a list of tasks for each employee. It then exports this data to a JSON file.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd employee-task-management
   ```

3. Ensure you have Python 3.x installed on your system.

4. Install the required Python libraries if not already installed:

   ```bash
   pip install requests
   ```

## Running the Scripts

To execute each script, open a terminal, navigate to the project directory, and run the desired script using Python. Replace `<employee_id>` with the actual ID of the employee for whom you want to perform the task.

Example usage for Task 0:

```bash
python3 0-gather_data_from_an_API.py 1
```

## Output Files

- Task 1 will create a CSV file named `<employee_id>.csv`.
- Task 2 will create a JSON file named `<employee_id>.json`.
- Task 3 will create a JSON file named `todo_all_employees.json`.

## API Endpoint

The scripts use the following API endpoint as the base URL:
```
https://jsonplaceholder.typicode.com
```

Make sure to replace this URL with the actual API endpoint you intend to use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
