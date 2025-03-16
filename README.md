# Docker Studies

This repository contains various Docker projects to demonstrate different use cases and configurations.

## Project Structure

- `hello-world-docker/`
  - `Dockerfile`: Docker configuration for a simple "Hello World" application.
  - `hello_world.py`: Python script that prints "Hello World" and the current time.

- `python-env/`
  - `app.py`: Python script that imports several data science libraries.
  - `Dockerfile`: Docker configuration for setting up a Python environment with specific dependencies.
  - `requirements.txt`: List of Python dependencies required for the `app.py` script.

- `streamlit-docker/`
  - `Dockerfile`: Docker configuration for a Streamlit application (not provided in the current workspace).

- `streamlit-local-docker/`

  - `app.py`: Streamlit application script.
  - `Dockerfile`: Docker configuration for setting up a local Streamlit application with Conda dependencies.
  - `environment.yaml`: Conda environment configuration file.


- `remote-sensing-jupyter-conda-env/`
  - `Dockerfile`: Docker configuration for setting up a Jupyter Notebook environment with Conda dependencies for remote sensing and geospatial projects.
  - `environment.yaml`: Conda environment configuration file.
