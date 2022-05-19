FROM python:3.9-bullseye

LABEL maintainer "Network Team <jakub.tadych@gmail.com>"

# updates and new installs
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils vim


# Copy python requirements file
RUN pip3 install --upgrade pip
COPY configs/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Create code folder
ADD . /code
WORKDIR /code
