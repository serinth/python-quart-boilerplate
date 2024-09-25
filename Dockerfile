FROM python:3.11.10-slim-bookworm
ENV WORK_ENV="DEV"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ./entrypoint.sh

