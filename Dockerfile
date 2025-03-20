# Use Ubuntu as the base image
FROM ubuntu:latest

# Install Python3, pip, and venv
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment and install Python libraries
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir pandas numpy seaborn matplotlib scikit-learn scipy

# Set the virtual environment as default
ENV PATH="/opt/venv/bin:$PATH"

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Copy the dataset to the container
COPY train_titanic.csv /home/doc-bd-a1/train_titanic.csv

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Set default command
CMD ["/bin/bash"]
