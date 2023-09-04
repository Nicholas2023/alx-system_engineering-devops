# Load Balancer Configuration :wink:

This repository contains scripts and instructions for configuring a load balancer (HAProxy) and web servers (Nginx) as part of a project. The goal is to distribute incoming HTTP requests among multiple web servers and add a custom HTTP response header to identify the server handling the request.

## Task 0: Configure Web Servers and Add Custom HTTP Response Header

### Script: 0-custom_http_response_header

This script configures web-01 and web-02 servers to meet the project requirements. It performs the following tasks:

1. Updates the package list and upgrades the system.
2. Installs Nginx.
3. Creates a custom Nginx configuration to add the `X-Served-By` HTTP response header.
4. Restarts Nginx to apply the changes.

Usage:

```bash
./0-custom_http_response_header
```

Make sure to run this script on both web-01 and web-02 servers to configure them.

## Task 1: Install and Configure HAProxy

### Script: 1-install_load_balancer

This script installs and configures HAProxy on the lb-01 server. It ensures that incoming HTTP traffic is evenly distributed between web-01 and web-02 servers using a round-robin algorithm. The script also sets up HAProxy to start on system boot.

Before running the script, replace `[web-01-IP]` and `[web-02-IP]` with the actual IP addresses of web-01 and web-02 servers.

Usage:

```bash
./1-install_load_balancer
```

Run this script on the lb-01 server to install and configure HAProxy.

## Repository Structure

- `0-custom_http_response_header`: Contains the script for Task 0.
- `1-install_load_balancer`: Contains the script for Task 1.

## Additional Notes

- Ensure that the hostnames of web-01 and web-02 servers are configured as `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02` to match the project requirements.
- For any issues or questions, please refer to the project's documentation or seek assistance.

Feel free to reach out if you have any questions or need further assistance with this project.
