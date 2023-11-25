#!/usr/bin/env bash
# Puppet module to configure SSH client settings

file {'/etc/ssh/ssh_config':
  ensure -> present,
}

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':,
  path   => '/home/your_username/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
