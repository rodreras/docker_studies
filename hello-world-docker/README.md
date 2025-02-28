# Hello World Docker

This project contains a simple "Hello World" application using Docker.

## Files

- `Dockerfile`: Docker configuration for the application.
- `hello_world.py`: Python script that prints "Hello World" and the current time.

## Instructions

To build and run the Docker container:

1. Navigate to the `hello-world-docker` directory:
    ```sh
    cd hello-world-docker
    ```

2. Build the Docker image:
    ```sh
    docker build -t hello-world .
    ```

3. Run the Docker container:
    ```sh
    docker run hello-world
    ```