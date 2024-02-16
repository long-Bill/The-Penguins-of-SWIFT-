FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo openssh-server -y 

USER root


RUN addgroup skipper
RUN addgroup private
RUN addgroup penguins


RUN useradd -m -d /home/skipper -s /bin/bash -g skipper -u 1001 skipper
RUN usermod -a -G penguins skipper
RUN echo "skipper:password" | chpasswd



RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER skipper

EXPOSE 22

WORKDIR /home/skipper