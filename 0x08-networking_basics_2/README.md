# Networking Basics :wink:

This repository contains Bash scripts for basic networking tasks on an Ubuntu server

## Contents
1. Change your home IP
2. Show attached IPs

## Change your home IP
This script (`0-change_your_home_IP`) configures Ubuntu server to change the IP address resolution for `localhost` and `facebook.com` as follows:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

### Usage:
```bash
./1-show_attached_IPs
```
The script will output the active IPv4 IPs on the machine.

## Requirements
- The scripts are tested on an Ubuntu server.
- Root privileges are required to run the `0-change_your_home_IP` script.

## Contributing
Contributions to improve and expand the functionality of the scripts are welcome! Please follow the contribution guidelines.

## License
This project is licensed under the MIT License.
