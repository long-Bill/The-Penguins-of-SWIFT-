FROM ubuntu:22.04

RUN addgroup gamer

RUN useradd -m -d /home/gamer -s /bin/bash -g gamer -u 1001 gamer

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc

COPY FirstFlag.txt /home/gamer/
RUN chown -R gamer:gamer /home/gamer/FirstFlag.txt

USER gamer

WORKDIR /home/gamer




