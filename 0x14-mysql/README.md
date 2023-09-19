# MySQL Setup and Replication Tasks :smile:

This repository contains scripts and instructions for setting up MySQL, creating users, databases, and configuring replication between two servers (primary and replica).

## Table of Contents

- [Task 0: Install MySQL](#task-0-install-mysql)
- [Task 1: Create a MySQL User](#task-1-create-a-mysql-user)
- [Task 2: Create a Database and Table](#task-2-create-a-database-and-table)
- [Task 3: Create a Replica User](#task-3-create-a-replica-user)
- [Task 4: Setup Primary-Replica Infrastructure](#task-4-setup-primary-replica-infrastructure)
- [Task 5: MySQL Backup (Bash Script)](#task-5-mysql-backup-bash-script)

## Task 0: Install MySQL

In this task, we install MySQL 5.7.x on both web-01 and web-02 servers. MySQL is a relational database management system.

### Instructions
1. Install MySQL 5.7.x on both web-01 and web-02 servers.
2. Verify the MySQL installation on both servers using the `mysql --version` command.

## Task 1: Create a MySQL User

In this task, we create a MySQL user named `holberton_user` on both web-01 and web-02 servers. This user is used for accessing and checking the replication status.

### Instructions
1. Create a MySQL user named `holberton_user` with the specified privileges.
2. Ensure that `holberton_user` has permission to check the primary/replica status of your databases.

## Task 2: Create a Database and Table

In this task, we create a database named `tyrell_corp` and a table named `nexus6` within the `tyrell_corp` database on web-01. We also add at least one entry to the table.

### Instructions
1. Create the `tyrell_corp` database and the `nexus6` table on web-01.
2. Add at least one entry to the `nexus6` table.
3. Grant `holberton_user` SELECT permissions on the `nexus6` table.

## Task 3: Create a Replica User

Before setting up replication, we create a new user named `replica_user` on web-01. This user is used by the replica server to connect to the primary server for replication.

### Instructions
1. Create a new user named `replica_user` on web-01 with appropriate replication privileges.
2. Ensure that `holberton_user` has SELECT privileges on the `mysql.user` table to check that `replica_user` was created with the correct permissions.

## Task 4: Setup Primary-Replica Infrastructure

In this task, we set up a primary-replica infrastructure using MySQL. The primary MySQL server is hosted on web-01, and the replica is hosted on web-02.

### Instructions
1. Modify the MySQL configuration on web-01 to enable replication.
2. Configure replication on web-02 to replicate data from web-01.
3. Check the replication status on both servers to ensure synchronization.

## Task 5: MySQL Backup (Bash Script)

To ensure data redundancy, we create a Bash script for generating MySQL backups. The script dumps all MySQL databases, compresses the dump, and stores it with a timestamp in the filename.

### Instructions
1. Run the Bash script `5-mysql_backup` with the MySQL root password as an argument to create backups.

## Contributors

- `Odhiambo Nicholas`

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the [ALX SE] - see the [LICENSE](LICENSE) file for details.
