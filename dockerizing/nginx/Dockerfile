FROM nginx
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN rm /etc/nginx/conf.d/default.conf
ADD dockerizing/nginx/sites-enabled/default.conf /etc/nginx/conf.d/default.conf
ADD dockerizing/nginx/ssl /etc/nginx/ssl_cert/
