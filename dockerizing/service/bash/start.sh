supervisord && memcached -d -m 128 -p 11211 -u root -l 127.0.0.1 && uwsgi /usr/src/myproject/django_uwsgi.ini