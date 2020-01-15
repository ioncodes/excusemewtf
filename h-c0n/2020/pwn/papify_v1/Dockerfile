FROM ubuntu:19.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y lib32z1 xinetd
RUN useradd -u 8888 -m pwn
CMD ["/usr/sbin/xinetd", "-dontfork"]
