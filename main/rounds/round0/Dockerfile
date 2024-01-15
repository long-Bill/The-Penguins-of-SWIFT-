FROM ubuntu:22.04

RUN addgroup gamer

RUN useradd -m -d /home/gamer -s /bin/bash -g gamer -u 1001 gamer

USER gamer


WORKDIR /home/gamer

COPY test.txt . 


