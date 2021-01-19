# Base Image
FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /practice

ADD . /practice

COPY ./requirements.txt ./practice/requirements.txt

RUN pip install -r requirements.txt

RUN mongod --dbpath ./practice/db/

RUN redis
# # create and set working directory
# RUN mkdir /practice
# WORKDIR /practice

# # Add current directory code to working directory
# ADD . /practice/

# # set default environment variables

# ENV LANG C.UTF-8
# ENV DEBIAN_FRONTEND=noninteractive 

# # set project environment variables
# # grab these via Python's os.environ
# # these are 100% optional here
# ENV PORT=8000

# # Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#         tzdata \
#         python3-setuptools \
#         python3-pip \
#         python3-dev \
#         python3-venv \
#         git \
#         && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*


# # install environment dependencies
# RUN pip3 install --upgrade pip 
# RUN pip3 install pipenv

# # Install project dependencies
# RUN pipenv install --skip-lock --system --dev

# EXPOSE 8000
# CMD gunicorn practice.wsgi:application --bind 0.0.0.0:$PORT