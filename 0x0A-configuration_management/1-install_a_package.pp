#!/usr/bin/pup
# Install Flask version 2.1.0 using pip3
package { 'python3':
  ensure => installed,
}
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
