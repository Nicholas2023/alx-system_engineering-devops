# Web Stack Debugging #1 :smile:

This repository contains a Bash script to fix an issue where Nginx is not listening on port 80 as expected. The script automates the process of configuring Nginx to listen on port 80 and ensures that the Nginx service is not running.

## Problem Description

When Nginx is not listening on port 80, it can prevent web traffic from being properly served. This repository provides a solution to this problem by creating a Bash script to reconfigure Nginx and restart the service.

## Solution

The solution consists of a Bash script (`1-debugging_made_short`) that performs the following steps:

1. Stops the Nginx service if it is currently running.
2. Modifies the default Nginx configuration to listen on port 80.
3. Starts the Nginx service to apply the changes.

## Usage

To use the provided Bash script to fix the Nginx configuration, follow these steps:

1. Clone this repository to your Ubuntu server or container.

   ```bash
   git clone https://github.com/Nicholas2023/alx-system_engineering-devops.git
   ```

2. Change into the directory containing the script.

   ```bash
   cd alx-system_engineering-devops/0x0E-web_stack_debugging_1
   ```

3. Make the script executable.

   ```bash
   chmod +x 1-debugging_made_short
   ```

4. Run the script to fix the Nginx configuration.

   ```bash
   ./1-debugging_made_short
   ```

This script will stop the Nginx service if it's running, modify the default Nginx configuration to listen on port 80, and then start the Nginx service again. After running the script, Nginx should be listening on port 80, and the `service nginx status` command should report that Nginx is not running.

## Requirements

- Ubuntu server or container.
- Superuser (root) privileges are required to execute the script.
- Nginx must be installed on the server/container.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
