FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 


RUN addgroup private
RUN addgroup king_julien
RUN addgroup mort


RUN useradd -m -d /home/private -s /bin/bash -g private -u 1001 private
RUN usermod -a -G sudo private
RUN echo "private:private" | chpasswd

RUN useradd -m -d /home/king_julien -s /sbin/nologin -g king_julien -u 1002 king_julien

RUN useradd -m -d /home/mort -s /sbin/nologin -g mort -u 1003 mort
COPY zoo.csv /home/mort/
RUN chmod -R 755 /home/mort



RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER private

WORKDIR /home/private




