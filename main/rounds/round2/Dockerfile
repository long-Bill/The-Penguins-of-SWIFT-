FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 


RUN addgroup private


RUN useradd -m -d /home/private -s /bin/bash -g private -u 1001 private
RUN usermod -a -G sudo private
RUN echo "private:private" | chpasswd

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER private

WORKDIR /home/private




