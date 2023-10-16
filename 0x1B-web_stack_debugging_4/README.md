# Web Stack Debugging #4 :wink:

## Task Description

In this web stack debugging task, the goal was to assess the performance of a web server setup featuring Nginx under pressure using ApacheBench. The server was experiencing a large number of failed requests, and the challenge was to reduce these failures to zero.

## Task 1: Server Optimization

### File: 0-the_sky_is_the_limit_not.pp

The initial benchmarking revealed 943 failed requests out of 2000. After analyzing the server setup, necessary fixes were implemented. The server configurations were adjusted using Puppet, enhancing the server's performance significantly.

#### Changes Made:

- **File Descriptor Limit:** Increased the file descriptor limit for the holberton user to resolve the "Too many open files" issue.

### Usage:

Apply the Puppet manifest to implement the changes:

```bash
puppet apply 0-the_sky_is_the_limit_not.pp
```

## Results after Optimization

- **Complete Requests:** 2000
- **Failed Requests:** 0
- **Requests per Second:** 6650.99 [#/sec] (mean)
- **Time per Request:** 0.150 [ms] (mean, across all concurrent requests)
- **Longest Request:** 31 ms

## Task 2: User Limit Fix

### File: 1-user_limit.pp

Fixed the issue where the holberton user encountered "Too many open files" error when trying to log in or open files. Puppet was used to modify the operating system configuration.

### Usage:

Apply the Puppet manifest to implement the changes:

```bash
puppet apply 1-user_limit.pp
```

## Author

*Nicholas Otieno Odhiambo*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
