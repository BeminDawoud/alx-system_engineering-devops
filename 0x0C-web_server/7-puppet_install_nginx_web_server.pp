# instal nginx
package { 'nginx':
provider => 'apt',
}
exec {'hello-page':
command => '/usr/bin/sudo /bin/echo "Hello World!" > /var/www/html/index.nginx-debian.html',
}
exec {'redirect_page':

command => '/usr/bin/sudo /bin/sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
}
exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}
