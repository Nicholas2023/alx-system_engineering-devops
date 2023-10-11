# Web Stack Monitoring with Datadog :smile:

This repository contains solutions for web stack monitoring tasks using Datadog, a powerful monitoring and analytics platform. The tasks include signing up for Datadog, installing the Datadog agent, setting up monitors for read and write requests, creating a dashboard, and generating an answer file with the dashboard ID.

## Tasks Overview

### Task 0: Sign up for Datadog and install datadog-agent
1. Sign up for a free Datadog account at [Datadog](https://app.datadoghq.com) using the US1 region.
2. Install the Datadog agent on the server `web-01`.
3. Create an application key in Datadog and update your Intranet user profile with the API key and application key.
4. Verify server visibility in Datadog using the provided API.
   
### Task 1: Monitor some metrics
1. Set up a monitor to track the number of read requests issued to the device per second.
2. Set up a monitor to track the number of write requests issued to the device per second.

### Task 2: Create a dashboard
1. Create a new Datadog dashboard.
2. Add at least 4 widgets to the dashboard to visualize various metrics.
3. Obtain the dashboard ID using Datadog's API and create the `2-setup_datadog` file with the dashboard ID.

## Repository Structure

- **Directory:** 0x18-webstack_monitoring
  - **Files:**
    - `2-setup_datadog`: Contains the dashboard ID generated for the created dashboard.
    - Other necessary files related to the tasks.
    
## Instructions for Running the Code

1. Clone the repository: `git clone https://github.com/username/alx-system_engineering-devops.git`
2. Navigate to the `0x18-webstack_monitoring` directory: `cd alx-system_engineering-devops/0x18-webstack_monitoring`
3. Follow the task instructions to complete the setup, monitors, and dashboard creation.
4. Ensure all changes are committed and pushed to the repository.

## Notes

- Make sure to follow the task instructions carefully to complete the setup and configurations.
- For any issues or questions, contact Nicholas Otieno at nicholasodhiambo2015@gmail.com.

Happy Monitoring!
