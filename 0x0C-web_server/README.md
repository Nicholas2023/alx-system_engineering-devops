# Web Server Configuration Tasks :wink:

This repository contains a set of Bash scripts to perform various configuration tasks related to setting up a web server using Nginx.

## Task 0: Transfer a File to the Server

The Bash script `0-transfer_file` transfers a file from the client to a server using the `scp` command. It accepts four parameters: the path to the file, the server's IP, the SSH username, and the path to the SSH private key.

Usage:
```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```

## Task 1: Install Nginx Web Server

The Bash script `1-install_nginx_web_server` installs Nginx on the web server and configures it to listen on port 80. It ensures that querying Nginx's root `/` with a GET request returns a page containing the string "Hello World!".

Usage:
```bash
./1-install_nginx_web_server > /dev/null 2>&1
```

## Task 2: Setup a Domain Name

The domain name is configured using the `2-setup_a_domain_name` script. It sets up DNS records with an A entry so that the root domain points to the web server's IP address. Note that DNS record propagation can take some time.

Example:
```bash
cat 2-setup_a_domain_name
YourDomainName.tech
```

## Task 3: Redirection

The `3-redirection` script configures Nginx to perform a 301 permanent redirection from the `/redirect_me` path to another page.

## Task 4: Not Found Page 404

The `4-not_found_page_404` script configures Nginx to display a custom 404 page with the message "Ceci n'est pas une page" when a page is not found.

---

**Note**: If you encounter any issues or need further assistance, you can check Nginx logs located in `/var/log/`.

**Repository**: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)

**Directory**: 0x0C-web_server

For more details, refer to the individual scripts in the repository.
