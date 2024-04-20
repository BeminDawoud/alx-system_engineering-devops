#!/usr/bin/pup
# script config for install flask.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
