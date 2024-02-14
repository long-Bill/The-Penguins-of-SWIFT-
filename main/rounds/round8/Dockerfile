FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 


RUN addgroup kowalski
RUN addgroup penguins
RUN addgroup mort
RUN addgroup king_julien


RUN useradd -m -d /home/kowalski -s /bin/bash -g kowalski -u 1001 kowalski
RUN usermod -a -G sudo kowalski
RUN echo "kowalski:kowalski" | chpasswd
RUN echo "%sudo  ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "Defaults        env_reset,timestamp_timeout=0" >> /etc/sudoers

RUN useradd -m -d /home/mort -s /bin/bash -g mort -u 1002 mort
RUN usermod -a -G penguins mort
RUN echo "mort:mort" | chpasswd
RUN useradd -m -d /home/king_julien -s /bin/bash -g king_julien -u 1003 king_julien
RUN usermod -a -G penguins king_julien
RUN echo "king_julien:king_julien" | chpasswd


RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER kowalski

WORKDIR /home/kowalski