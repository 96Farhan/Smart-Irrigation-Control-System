# Pull the base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
#Upgrade pip
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev libgeos-dev -y
RUN pip3 install pip -U
ADD requirements.txt /code/
#Install dependencies
RUN pip3 install -r requirements.txt
COPY ./entrypoint.sh /code/entrypoint.sh
ADD . /code/
# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]