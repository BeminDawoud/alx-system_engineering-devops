#!/usr/bin/pup
# Install Flask version 2.1.0 using pip3
package { 'pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
