# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

#Set the trace level for app
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0

# Copy local code to the container image.
ENV APP_HOME /app
ENV PORT 3000
ENV TRACE_LEVEL 0
ENV UMBRAL .86
WORKDIR $APP_HOME
COPY . ./
COPY requirements.txt ./

# Install production dependencies.
# RUN pip install ffmpeg-downloader
# RUN ffdl install --add-path
RUN apt-get -y update
# RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN apt-get install flac
RUN pip install -r requirements.txt
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --chdir=./src/ --workers 1 --threads 8 --timeout 0 app:app