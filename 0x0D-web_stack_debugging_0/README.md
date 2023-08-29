# Web Stack Debugging #0 :smile:

In this project, the goal is to debug and fix an issue related to getting Apache to run in a Docker container and return a page containing "Hello Holberton" when querying the root of the container.

## Project Structure

- `Dockerfile`: Contains the instructions to build a Docker image that runs Apache and serves the "Hello Holberton" page.
- `src/`: Directory containing the HTML file to be served by Apache.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Docker: Make sure you have Docker installed on your system.

### Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo/0x0D-web_stack_debugging_0
   ```

2. Create the `src` directory and the `index.html` file:

   ```bash
   mkdir src
   echo '<!DOCTYPE html><html><head><title>Hello Holberton</title></head><body><h1>Hello Holberton</h1></body></html>' > src/index.html
   ```

3. Build the Docker image:

   ```bash
   docker build -t my-apache-image .
   ```

4. Run the Docker container and map port 8080 to port 80:

   ```bash
   docker run -p 8080:80 -d my-apache-image
   ```

5. Access the "Hello Holberton" page:

   Open a web browser or use `curl` to access the page:

   ```bash
   curl 0:8080
   ```

   You should see the "Hello Holberton" message displayed.

## Troubleshooting

If you encounter any issues while setting up the project, consider the following tips:

- Make sure Docker is properly installed and running on your system.
- Double-check the Dockerfile and ensure it copies the `src` directory correctly.
- Verify that there are no errors or issues during the Docker image build process.
- If you're using an existing container, ensure that the Apache service is started within the container.

## Author

[Nicholas Otieno](https://github.com/Nicholas2023)

Feel free to reach out if you have any questions or need further assistance!
