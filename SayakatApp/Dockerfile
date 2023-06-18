# pull official base image
FROM python:3.9.6-alpine

RUN apk update \
    && apk upgrade  \
    && apk add --no-cache bash \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add --no-cache mysql-client

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Convert plain text files from Windows or Mac format to Unix
RUN apk add --no-cache dos2unix
RUN dos2unix --newfile ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Make entrypoint executable
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Entrypoint dependencies
RUN apk --no-cache add nmap-ncat

# run entrypoint.sh
ENTRYPOINT ["bash", "/usr/local/bin/docker-entrypoint.sh"]

# Set the default command for the container
CMD ["/bin/bash"]
