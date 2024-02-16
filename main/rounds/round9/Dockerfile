FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo cron -y 

USER root


RUN addgroup kowalski
RUN addgroup penguins


RUN useradd -m -d /home/kowalski -s /bin/bash -g kowalski -u 1001 kowalski
RUN usermod -a -G sudo kowalski
RUN echo "kowalski:kowalski" | chpasswd

RUN touch /root/counter.txt
ADD user.sh /root/user.sh
RUN chmod 0744 /root/user.sh
ADD timer.sh /root/timer.sh
RUN chmod 0744 /root/timer.sh

RUN crontab -l | { cat; echo "*/1 * * * * bash /root/timer.sh"; } | crontab -


RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER kowalski

WORKDIR /home/kowalski

