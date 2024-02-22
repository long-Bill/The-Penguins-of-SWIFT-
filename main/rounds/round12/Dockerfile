FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo apache2 -y 

USER root


RUN addgroup skipper
RUN addgroup penguins


RUN useradd -m -d /home/skipper -s /bin/bash -g skipper -u 1001 skipper
RUN usermod -a -G penguins,sudo skipper
RUN echo "skipper:skipper" | chpasswd

COPY skipperIndex.html /var/log/index.html
COPY ricoIndex.html /var/www/html/index.html
COPY rico.jpeg /var/www/html/rico.jpeg

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc

EXPOSE 80

USER skipper



WORKDIR /home/skipper
