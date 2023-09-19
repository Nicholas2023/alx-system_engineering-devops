# Web Stack Debugging #2 :wink:

This repository contains Bash scripts and instructions for debugging and configuring a web server.

## Task 0: iamsomeoneelse

The `0-iamsomeoneelse` script allows you to run a command as another user. Simply provide the username as an argument, and it will execute the `whoami` command under the specified user.

Usage:
```bash
./0-iamsomeoneelse <username>
```

## Task 1: Run Nginx as Nginx

In this task, we fix a container configuration to run Nginx as the less privileged `nginx` user. This enhances security by limiting the impact of potential security breaches.

**Requirements:**
- Nginx must be running as the `nginx` user.
- Nginx must listen on all active IPs on port 8080.

Usage:
```bash
./1-run_nginx_as_nginx
```

After running the script, you can verify the Nginx user and port with the following commands:
```bash
ps auxff | grep ngin[x]
nc -z 0 8080 ; echo $?
```

## Task 2: 7 Lines or Less

Task 2 provides a more concise solution to the problem addressed in Task 1. The Bash script must be no longer than 7 lines and should follow the same requirements as Task 1.

Usage:
```bash
./100-fix_in_7_lines_or_less
```

## Repository Structure

- `0-iamsomeoneelse`: Task 0 Bash script.
- `1-run_nginx_as_nginx`: Task 1 Bash script.
- `100-fix_in_7_lines_or_less`: Task 2 Bash script.
- `README.md`: This documentation.
