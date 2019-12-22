FROM ubuntu:18.04

COPY files /app
COPY flag /flag

WORKDIR /app

RUN apt-get update && apt-get install -y socat
RUN useradd -UM chall

CMD /app/start.sh
