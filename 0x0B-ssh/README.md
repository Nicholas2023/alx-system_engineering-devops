# SSH Tasks

This repository contains scripts and configuration files related to SSH for the ALX System Engineering DevOps course.

## Task 0: Use a Private Key

### Description
This script establishes an SSH connection to a server using a specific private key and user.

### Requirements
- Connect to the server using SSH with single-character flags.
- Use the private key located at `~/.ssh/school`.
- Connect as the `ubuntu` user.

### Usage
```bash
./0-use_a_private_key
```

## Task 1: Create an SSH Key Pair

### Description
This script generates an RSA key pair with specific requirements.

### Requirements
- Create an RSA key pair.
- Name the private key `school`.
- Use 4096 bits for the key size.
- Protect the key with the passphrase "betty".

### Usage
```bash
./1-create_ssh_key_pair
```

## Task 2: Client Configuration File

### Description
This task involves configuring the local SSH client using the SSH configuration file.

### Requirements
- Configure the SSH client to use the private key `~/.ssh/school`.
- Configure the SSH client to refuse password-based authentication.

## Task 3: Let Me In!

### Description
This task requires adding a public key to the server's authorized keys for SSH access.

Feel free to use these scripts and configuration files for your SSH-related tasks. If you have any questions or need further assistance, don't hesitate to reach out.
