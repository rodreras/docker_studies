# Remote Sensing Jupyter Conda Environment

This project sets up a Jupyter Notebook environment with Conda dependencies for remote sensing  and geospatial projects using Docker.

## Files

- `Dockerfile`: Docker configuration for setting up the Jupyter Notebook environment.
- `environment.yml`: Conda environment configuration file.

## Instructions

### Build the Docker Image

1. Navigate to the `remote-sensing-jupyter-conda-env` directory:
    ```sh
    cd remote-sensing-jupyter-conda-env
    ```

2. Build the Docker image:
    ```sh
    docker build -t remote-sensing-jupyter .
    ```

### Deploy the Docker Container

1. Run the Docker container:
    ```sh
    docker run -it -p 8888:8888 remote-sensing-jupyter
    ```

2. Open your web browser and navigate to the URL provided in the terminal output (usually `http://localhost:8888`) to access the Jupyter Notebook interface.

