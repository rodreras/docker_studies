# Streamlit Docker

This project sets up a Streamlit application using Docker.

## Files

- `Dockerfile`: Docker configuration for the Streamlit application.

## Instructions

To build and run the Docker container:

1. Navigate to the `streamlit-docker` directory:
    ```sh
    cd streamlit-docker
    ```

2. Build the Docker image:
    ```sh
    docker build -t streamlit-app .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 8501:8501 streamlit-app
    ```