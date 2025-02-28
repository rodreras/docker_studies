# Python Environment Docker

This project sets up a Python environment with specific dependencies using Docker.

## Files

- `Dockerfile`: Docker configuration for setting up the Python environment.
- `app.py`: Python script that imports several data science libraries.
- `requirements.txt`: List of Python dependencies required for the `app.py` script.

## Instructions

To build and run the Docker container:

1. Navigate to the `python-env` directory:
    ```sh
    cd python-env
    ```

2. Build the Docker image:
    ```sh
    docker build -t python-env .
    ```

3. Run the Docker container:
    ```sh
    docker run python-env
    ```