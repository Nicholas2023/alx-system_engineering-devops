# Application Server Configuration and Deployment :smile:

This repository contains the configurations and scripts for setting up an application server for an AirBnB clone project. The server is configured using Flask, Gunicorn, and Nginx, and includes provisions for handling deployments without downtime.

## Task List

### 1. Set up development with Python

- Ensure SSH access to the server (complete task #3 of SSH project).
- Install the `net-tools` package: `sudo apt install -y net-tools`.
- Git clone the AirBnB_clone_v2 repository to `web-01` server.
- Configure `web_flask/0-hello_route.py` to serve content from the route `/airbnb-onepage/` on port 5000.

### 2. Set up production with Gunicorn

- Install Gunicorn and required libraries.
- Configure Gunicorn to serve content from the same route as the previous task.
- Bind Gunicorn instance to `0.0.0.0:5000`.
- Ensure nothing is listening on port 6000 for checker verification.

### 3. Serve a page with Nginx

- Configure Nginx to serve content from the route `/airbnb-onepage/`.
- Proxy requests to the Gunicorn process listening on port 5000.
- Nginx should serve the page both locally and on its public IP on port 80.

### 4. Add a route with query parameters

- Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001.

### 5. Serve AirBnB clone - Web dynamic

- Git clone the AirBnB_clone_v4 repository.
- Configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Set up Nginx to proxy requests to Gunicorn.
- Ensure Nginx serves static assets from `web_dynamic/static/`.
- Update `web_dynamic/static/scripts/2-hbnb.js` to correct IP address.

### 6. Deploy with Systemd

- Write a systemd script to start Gunicorn with 3 worker processes.
- Log errors in `/tmp/airbnb-error.log` and access in `/tmp/airbnb-access.log`.
- Bind Gunicorn to port 5003.
- Store the systemd script in the appropriate directory on `web-01`.

### 7. No service interruption

- Write a Bash script to reload Gunicorn gracefully, allowing updates without downtime.
- Test the script by rebooting the server (`sudo reboot`) and ensuring a seamless transition.

## Usage

- Clone this repository to your local machine or server.
- Follow the instructions provided in each task to set up and configure the application server.

## Notes

- This configuration is designed for educational purposes and may need adjustments for production use.
- Ensure proper security measures are in place before deploying any application to a public server.
