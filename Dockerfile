FROM python:3.6

ENV PYTHONDONTWRITEBYTECOE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get -y install build-essential cmake libgtk-3-dev libboost-all-dev

WORKDIR /ar

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY websocket_server_un.py ./

COPY images ./images

ENTRYPOINT ["tail -f /dev/null"]