FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo openssh-server -y 

USER root


RUN addgroup skipper
RUN addgroup myguest
RUN addgroup penguins


RUN useradd -m -d /home/skipper -s /bin/bash -g skipper -u 1001 skipper
RUN usermod -a -G penguins,sudo skipper
RUN echo "skipper:skipper" | chpasswd

RUN useradd -m -d /home/myguest -s /bin/bash -g myguest -u 1002 myguest
RUN usermod -a -G penguins myguest
RUN echo "myguest:myguest" | chpasswd
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication no/g' /etc/ssh/sshd_config

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc

EXPOSE 22
USER skipper



WORKDIR /home/skipper
