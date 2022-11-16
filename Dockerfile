# pull official base image
FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# File Author / Maintainer
LABEL org.opencontainers.image.authors="kg7pnh@arrl.net"

# add project files to the /app folder
ADD . /app

# set directoty where CMD will execute
WORKDIR /app
COPY ./requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt

# Collect static
RUN command python3 manage.py collectstatic --noinput

# Expose ports
EXPOSE 8000

# default command to execute
CMD exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3