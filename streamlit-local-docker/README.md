# Streamlit Local Docker

This project sets up a local Streamlit application with Conda dependencies using Docker.

## Files

- `Dockerfile`: Docker configuration for setting up the local Streamlit application.
- `app.py`: Streamlit application script.
- `environment.yaml`: Conda environment configuration file.

## Instructions

To build and run the Docker container:

1. Navigate to the `streamlit-local-docker` directory:
    ```sh
    cd streamlit-local-docker
    ```

2. Build the Docker image:
    ```sh
    docker build -t streamlit-local-app .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 8501:8501 -v $(pwd):/app streamlit-local-docker:latest 
    ```