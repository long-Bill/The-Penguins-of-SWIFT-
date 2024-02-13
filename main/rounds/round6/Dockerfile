FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo -y 


RUN addgroup central_park
RUN addgroup skipper
RUN addgroup rico
RUN addgroup private

RUN useradd -m -d /home/private -s /bin/bash -g private -u 1001 private
RUN usermod -a -G central_park,sudo private
RUN echo "private:private" | chpasswd

RUN useradd -m -d /home/skipper -s /sbin/login -g skipper -u 1002 skipper
RUN usermod -a -G central_park skipper
RUN mkdir /home/skipper/Documents/ 
RUN mkdir /home/skipper/Downloads/ 
COPY Julien_Spy.txt /home/skipper/


RUN useradd -m -d /home/rico -s /sbin/nologin -g rico -u 1003 rico
RUN usermod -a -G central_park rico
RUN mkdir /home/rico/Documents/ 
RUN mkdir /home/rico/Downloads/ 
COPY Julien_Spy.txt /home/rico/

RUN chown -R "skipper:central_park" /home/skipper/
RUN chown -R "skipper:central_park" /home/rico/


RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc
RUN chmod 150 -R /home/skipper/
RUN chmod 150 -R /home/rico/





USER private

WORKDIR /home/private
