FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 



RUN addgroup private
RUN addgroup penguins


RUN useradd -m -d /home/private -s /bin/bash -g private -u 1001 private
RUN usermod -a -G penguins,sudo private
RUN echo "private:private" | chpasswd
RUN useradd -m -d /home/skipper -s /sbin/nologin -g penguins -u 1002 skipper
RUN chmod 770 -R /home/skipper


RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc
COPY Route-To-Madagascar.txt /usr/bin/


USER private

WORKDIR /home/private