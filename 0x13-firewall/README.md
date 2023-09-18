# Firewall and Port Forwarding Setup on web-01 :smile:

This README.md file provides instructions for configuring the `ufw` firewall on `web-01` to block all incoming traffic except for specific TCP ports (22, 80, and 443), and for setting up port forwarding from port 8080 to port 80.

## Firewall Configuration

### Step 1: Install `ufw` (if not already installed)

If `ufw` is not already installed, you can install it with the following commands:

```bash
sudo apt-get update
sudo apt-get install ufw
```

### Step 2: Configure `ufw` to Allow Specific Ports

Allow incoming traffic on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS) while blocking all other incoming traffic. Run the following commands:

```bash
# Allow SSH (Port 22)
sudo ufw allow 22/tcp

# Allow HTTP (Port 80)
sudo ufw allow 80/tcp

# Allow HTTPS (Port 443)
sudo ufw allow 443/tcp

# Block all other incoming traffic
sudo ufw default deny incoming
```

### Step 3: Enable `ufw`

Enable `ufw` with the following command:

```bash
sudo ufw enable
```

### Step 4: Check `ufw` Status (Optional)

You can check the status of `ufw` to ensure that it is configured correctly:

```bash
sudo ufw status
```

### Port Forwarding Configuration

### Step 5: Configure Port Forwarding

To configure port forwarding from port 8080 to port 80, follow these steps:

1. Edit the `ufw` configuration file:

```bash
sudo nano /etc/ufw/before.rules
```

2. Add the following lines before the `*filter` section in the file:

```bash
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```

3. Save the file and exit the text editor.

### Step 6: Reload `ufw`

Reload `ufw` to apply the changes:

```bash
sudo ufw reload
```

### Step 7: Verify Port Forwarding

You can verify that port forwarding is working by using `curl` from another server:

```bash
curl -sI web-01.holberton.online:80
```

And also test port 8080:

```bash
curl -sI web-01.holberton.online:8080
```

You should see HTTP 200 responses for both ports.

Your `ufw` firewall on `web-01` is now configured to block all incoming traffic except for ports 22, 80, and 443, and it is forwarding traffic from port 8080 to port 80.

## Author

`Odhiambo Nicholas`

## License

This project is licensed under the [MIT License](LICENSE).
