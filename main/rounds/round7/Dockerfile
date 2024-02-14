FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 


RUN addgroup kowalski
RUN addgroup penguins



RUN useradd -m -d /home/kowalski -s /bin/bash -g kowalski -u 1001 kowalski
RUN echo "kowalski:kowalski" | chpasswd
RUN echo "alias ls='echo \"Melman was not here\"'" >> /home/kowalski/.bashrc
RUN echo "alias cat='echo \"Melman has a healthy neck\"'" >> /home/kowalski/.bashrc
RUN echo "alias cd='echo \"If I cant get a raise then you cant move\"'" >> /home/kowalski/.bashrc
RUN echo "alias grep='echo \"Theres no point in searching\"'" >> /home/kowalski/.bashrc


RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER kowalski

WORKDIR /home/kowalski