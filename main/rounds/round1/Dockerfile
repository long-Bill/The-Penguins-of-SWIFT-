FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install vim -y



RUN addgroup money

RUN useradd -m -d /home/money -s /bin/bash -g money -u 1001 money

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc

COPY FirstFlag.txt /home/money/
RUN chown -R money:money /home/money/FirstFlag.txt

USER money

WORKDIR /home/money