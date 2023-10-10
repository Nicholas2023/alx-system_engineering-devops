### Web Stack Debugging #3 :smile:

This repository contains the solution for the Web Stack Debugging #3 task. The task involves using `strace` to find out why Apache is returning a 500 error, fixing the issue, and then automating the fix using Puppet.

### Task Description

#### Step 1: Use `strace` to Find the Issue
- Use `strace` to attach to the running Apache process and identify the cause of the 500 Internal Server Error.

#### Step 2: Fix the Issue
- Fix the problem identified using `strace`. It could be related to file permissions, missing files, or other issues within the Apache configuration.

#### Step 3: Write Puppet Manifest to Automate the Fix
- Create a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix. Use Puppet resource types to apply the necessary configurations and ensure the issue is resolved.

#### Step 4: Apply the Puppet Manifest
- Apply the Puppet manifest using the `puppet apply` command to automate the fix for the Apache server.

### Files in the Repository
- **`0-strace_is_your_friend.pp`**: Puppet manifest file containing the code to fix the identified issue on Apache server.
- **`README.md`**: Documentation file providing an overview of the task and instructions to solve it.

### Instructions for Running the Solution

1. **Identify the Issue with `strace`**: Attach `strace` to the running Apache process and identify the cause of the 500 error.

2. **Fix the Issue Manually**: Manually fix the problem identified using `strace`. It could be related to file permissions, missing files, or other issues within the Apache configuration.

3. **Automate the Fix with Puppet**:
   - Modify `0-strace_is_your_friend.pp` to include the Puppet code necessary to fix the issue identified in Step 1.
   - Ensure to replace placeholder values in the Puppet manifest with actual paths, ownerships, permissions, and other parameters relevant to your system and issue.

4. **Apply the Puppet Manifest**:
   ```bash
   sudo puppet apply 0-strace_is_your_friend.pp
   ```

5. **Verify the Fix**:
   - Send a request to Apache to ensure the issue is resolved:
   ```bash
   curl -I 127.0.0.1
   ```
