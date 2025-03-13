# 1. Importing the Miniconda image from a linux amd64 archtecture 
FROM --platform=linux/amd64 continuumio/miniconda3:main

# 2. Defining the arguments.
ARG PYTHON_VERSION=3.10
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 3. Defining the system variables

#-- a. Installing and Updating basics
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  curl \
  git \
  vim \
  nano \
  wget \
  sudo \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

#-- b. Adding the arguments to the system
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME


#-- c. Copying the environment file to the image.
COPY environment.yml /tmp/environment.yml

#-- d. Configure the conda environment
RUN conda update -n base -c defaults conda \
&& conda config --append channels conda-forge \
&& conda env create -f /tmp/environment.yml \
&& conda clean -a -y 

#-- e. Conda Env Automatic activation
RUN conda init bash && \
    echo 'eval "$(conda shell.bash hook)"' >> /home/$USERNAME/.bashrc && \
    echo "conda activate rs_env" >> /home/$USERNAME/.bashrc

# 4. Setting the workdir
WORKDIR /workdir

# 5. Create dir for projects and adjust permissions
RUN mkdir -p /workspace/projects && \
  chown -R $USERNAME:$USERNAME /workspace

# 6. Change the directory to non-root
USER $USERNAME

# 7. Define shell as bash
SHELL [ "/bin/bash", "-c"]

# 8. Define the enter point of the container
CMD ["/bin/bash"]