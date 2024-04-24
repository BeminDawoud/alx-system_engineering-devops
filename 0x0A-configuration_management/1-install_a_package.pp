#!/usr/bin/pup
# Install Flask version 2.1.0 using pip3
package { 'python3-pip':
  ensure => installed,
}
package { 'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
