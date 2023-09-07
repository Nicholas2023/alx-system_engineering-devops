# HTTPS SSL Configuration with HAProxy :smile:

This repository contains the instructions and scripts for configuring HTTPS SSL termination with HAProxy for a domain and its subdomains.

## Task 0: World Wide Web - Bash Script

### Script Usage

To use the Bash script, follow these steps:

1. Make the script executable:

   ```bash
   chmod +x 0-world_wide_web.sh
   ```

2. Run the script with the domain and subdomain arguments:

   ```bash
   ./0-world_wide_web.sh yourdomain.com subdomain
   ```

   If you don't provide a subdomain, it will display information for the default subdomains: www, lb-01, web-01, and web-02.

### Example

```bash
./0-world_wide_web.sh yourdomain.com web-02
```

## Task 1: HAProxy SSL Termination

### Requirements

- HAProxy version 1.5 or higher.
- An SSL certificate obtained using Certbot.

### Installation and Configuration

1. Install HAProxy:

   ```bash
   sudo apt-get update
   sudo apt-get install haproxy
   ```

2. Obtain an SSL certificate using Certbot:

   ```bash
   sudo certbot certonly --standalone -d www.yourdomain.com
   ```

3. Edit the HAProxy configuration file:

   ```bash
   sudo nano /etc/haproxy/haproxy.cfg
   ```

4. Update the configuration as shown in `1-haproxy_ssl_termination.cfg`:

   ```haproxy
   [Paste the contents of 1-haproxy_ssl_termination.cfg here]
   ```

   Make sure to replace `www.yourdomain.com` with your actual domain.

5. Restart HAProxy to apply the changes:

   ```bash
   sudo service haproxy restart
   ```

6. Ensure your web server serves content with "Holberton School" on port 80.

### Testing

You can test the SSL termination by running:

```bash
curl -sI https://www.yourdomain.com
```

### Example

```bash
curl https://www.yourdomain.com
```

## Task 2: Redirect HTTP to HTTPS

### Configuration

To automatically redirect HTTP traffic to HTTPS, add the following to your HAProxy configuration file:

```haproxy
[Add the HTTP to HTTPS redirection configuration here]
```

7. Restart HAProxy to apply the redirection:

   ```bash
   sudo service haproxy restart
   ```

Now, when users visit your website using HTTP, they will be automatically redirected to HTTPS.

Replace `www.yourdomain.com` with your actual domain in all configurations.

**Note:** Ensure that your server and SSL certificate are correctly set up for secure HTTPS connections.
