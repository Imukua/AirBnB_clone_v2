#!/usr/bin/env bash
# Set up nginx server for the web static deployement

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Alx-school Rocks" > /data/web_static/releases/test/index.html
ln -snf /data/web_static/releases/test/ /data/web_static/current
chown --recursive ubuntu:ubuntu /data/


printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://github.com/Imukua;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart