# Processes and Signals :smile:

This project focuses on understanding processes and signals in Linux. It includes several Bash scripts that demonstrate different aspects of process management. The scripts are designed to run on Ubuntu 20,04 LTS and have been tested for compliance with various requirements.

## Learning Objectives

By completing this project, you will gain a solid understanding of the following concepts:
- What is a PID(Process ID)?
- What is a process?
- How to find process' PID
- How to kill a process
- What is a signal and how it is used in process management
- The significance of two signals that cannot be ignored

## Requirement
- Allowed editors: vi, vim, emacs
- All files should be interpreted on Ubuntu 20.04 LTS
- All files must end with a new line
- A README.md file must be present at the root of the project directory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.7.0) without any errors
- The first line of all Bash scripts should be #!/usr/bin/env bash
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Project Structure
 
The project consists of the following files:
1. `0-what-is-my-pid`: Bash script that displays its own PID.
2. `1-list_your_processes`: Bash script that displays a list of currently running processes.
3. `2-show_your_bash_pid`: Bash script that displays lines containing the word "bash" to find the PID of the Bash process.
4. `3-show_your_bash_pid_made_easy`: Bash script that displays the PID and process name for processes containing the word "bash".
5. `4-to_infinity_and_beyond`: Bash script that displays "To infinity and beyond" indefinitely.
6. `5-dont_stop_me_now`: Bash script that demonstrates how to stop a process without using Ctrl+C.

## Usage
To use any of the Bash scripts, navigate to the project directory and execute the script using the command line. For example:

```.bash
./0-what-is-my-pid
```

The output will be displayed based on the functionality of the script.

**Note**: Some scripts may require additional steps or provide further instructions within the script itself

## Contributions

Contributions to the project are not allowed as per the program's guidelines. The project is intended for learning purposes only, and any form of plagiarism or unauthorized distribution of the content is strictly prohibited.

## License

This project is not licensed and is solely for educational purposes.
