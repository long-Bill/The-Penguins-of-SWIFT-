FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano -y 


RUN addgroup private
RUN addgroup penguins
RUN addgroup skipper


RUN useradd -m -d /home/private -s /bin/bash -g private -u 1001 private
RUN usermod -a -G penguins private

RUN useradd -m -d /home/skipper -s /bin/bash -g skipper -u 1002 skipper

COPY end.txt middle.txt party.txt part2.txt /home/skipper/
RUN chown -R "skipper:penguins" /home/skipper/
RUN chmod 770 -R /home/skipper/

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc


USER private

WORKDIR /home/private




