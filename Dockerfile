FROM ubuntu:latest

RUN apt update

RUN apt install -y python3 python3-pip

COPY . /data

WORKDIR /data

CMD ["python3", "program.py"]
