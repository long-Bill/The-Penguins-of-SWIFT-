FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install nano sudo apache2 -y 

USER root


RUN addgroup skipper
RUN addgroup penguins


RUN useradd -m -d /home/skipper -s /bin/bash -g skipper -u 1001 skipper
RUN usermod -a -G penguins,sudo skipper
RUN echo "skipper:skipper" | chpasswd


COPY skipperIndex.html /var/www/html/index.html
RUN chown -R www-data:www-data /var/www/html/
RUN chmod -R 760 /var/www/html/

RUN mkdir /var/www/HelloWorld
COPY helloIndex.html /var/www/HelloWorld/index.html
RUN chown -R www-data:www-data /var/www/HelloWorld/
RUN chmod -R 760 /var/www/HelloWorld/

RUN mkdir /var/www/Comrades
COPY comradeIndex.html /var/www/Comrades/index.html
RUN chown -R www-data:www-data /var/www/Comrades/
RUN chmod -R 760 /var/www/Comrades/
COPY smile.jpeg /var/www/Comrades/smile.jpeg

COPY hello.conf /etc/apache2/sites-available/hello.conf
COPY comrades.conf /etc/apache2/sites-available/Comrades.conf

RUN rm -rf /usr/bin/su

RUN echo "alias exit='echo \"NONE SHALL LEAVE, OR ELSE\"'" >> /etc/bash.bashrc

EXPOSE 80

USER skipper

WORKDIR /home/skipper
