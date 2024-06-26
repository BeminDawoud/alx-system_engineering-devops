# automated setup

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => ' IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => ' PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}
