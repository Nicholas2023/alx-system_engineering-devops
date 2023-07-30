# Web infrastructure Design Project  :smile:
This project aims to design a scalable and reliable web infrastructure for hosting the websites www.foobar.com. The infrastructure is designed to evolve from a simple one-server setup to a distributed setup with enhanced security, encryption and monitoring.

## Task 0: Simple Web Stack

### Overview
The task involves designing a simple web infrastructure using server with a LAMP stack(Linux, Apache, MySQL, PHP) to host the website www.foobar.com

## Components
### 1. Server:
A physical computer hosting the entire web infrastructure

### 2. Domain Name:
A human-readable address pointing to the server's IP address(e.g,8.8.8.8)

### 3. DNS Record:
A CNAME record for www pointing to the server's IP address

### 4. Web Server (Nginx):
Handles incoming HTTP requests and serves web pages

### 5. Application Server:
A processes dynamic content and executes server-side code

### 6. Application Files:
Contains the website's codebase and functionality

### 7. Database(MySQL):
Stores and manages website data


## Issues

### 1. SPOF (Single Point of Failure):
Entire infrastructure relies on a single server

### 2. Downtime during Maintenance:
Web server restarts lead to website unavailability

### 3. Scalability:
Limited capacity to handle high incoming traffic

## Task 2: Secured and Monitored Web Infrastructure
### Overview
This task further enhances the infrastructure with security measures and monitoring components.

### Components
### 1. Three Firewalls:
Provides security by controlling incoming and outgoing traffic.
### 2. SSL Certificate:
Enables HTTPS to secure data transmission.
### 3. Monitoring Clients:
Collects data and metrics for performance monitoring.

##Issues
### 1. SSL Termination at Load Balancer:
SSL termination should be done at the application servers.
### 2. Single MySQL Server for Writes:
A single point of failure for write operations.
### 3. Identical Components on Servers:
Uniform vulnerabilities across servers.

## Conclusion
By completing these tasks, we have designed a progressively more robust, secure, and scalable web infrastructure. The final setup is capable of handling high traffic, providing encrypted communication, and offering effective monitoring for improved reliability and performance.

Please refer to the individual task directories for more details on the design and components used in each infrastructure setup.
