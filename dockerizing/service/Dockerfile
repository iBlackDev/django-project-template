FROM python:3.7.3

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

ADD requirements.txt /opt/django/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r /opt/django/app/requirements.txt

RUN apt-get update 
RUN apt-get install -y supervisor
RUN apt-get install -y memcached

ADD dockerizing/service/bash/start.sh /usr/bin/start.sh
RUN chmod +x /usr/bin/start.sh

ADD dockerizing/service/etc/supervisor.conf /etc/supervisor/conf.d
RUN touch /var/log/celery_worker.log
RUN touch /var/log/celery_beat.log
RUN touch /var/log/celerycam.log
RUN touch /var/log/uwsgi.log
RUN touch /var/log/log.log

RUN mkdir /usr/src/myproject
WORKDIR /usr/src/myproject
CMD /usr/bin/start.sh