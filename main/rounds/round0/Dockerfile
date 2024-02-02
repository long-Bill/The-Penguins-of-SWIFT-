FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano -y 




RUN addgroup private


RUN useradd -m -d /home/private -s /bin/bash -g private -u 1001 private

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc

COPY MyMessage.txt /home/private/
RUN chown -R private:private /home/private/MyMessage.txt

USER private

WORKDIR /home/private




