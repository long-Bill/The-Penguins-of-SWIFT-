FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 

USER root


RUN addgroup kowalski
RUN addgroup skipper
RUN addgroup private
RUN addgroup penguins


RUN useradd -m -d /home/kowalski -s /bin/bash -g kowalski -u 1001 kowalski
RUN usermod -a -G sudo kowalski
RUN echo "kowalski:kowalski" | chpasswd


RUN useradd -m -d /home/skipper -s /bin/bash -g skipper -u 1002 skipper
RUN usermod -a -G penguins skipper
RUN echo "skipper:password" | chpasswd

RUN useradd -m -d /home/private -s /bin/bash -g private -u 1003 private
RUN usermod -a -G penguins private
RUN echo "private:password" | chpasswd

RUN mv /usr/bin/passwd /usr/bin/passwd.old
ADD passwd.sh /usr/bin/passwd
RUN chmod +x /usr/bin/passwd


RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER kowalski

WORKDIR /home/kowalski