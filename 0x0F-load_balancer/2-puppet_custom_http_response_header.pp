#install nginx
package { 'nginx':
ensure => present,
}

file_line { 'add_custom_header':
  line  => 'add_header X-Served-By $HOSTNAME;',
  path  => '/etc/nginx/sites-available/default',
  match => '^listen 80 default_server',
}
exec {'reload_server':

command => '/usr/bin/sudo /usr/sbin/service nginx restart',
}
