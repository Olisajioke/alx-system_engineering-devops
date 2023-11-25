#!/usr/bin/env bash
# Puppet module to configure SSH client settings
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config', # Path to the SSH server config file
  line   => 'PasswordAuthentication no', # Set PasswordAuthentication to no
  match  => '^#?PasswordAuthentication', # Match the line regardless of comments
}

file_line { 'Declare identity file':
  path   => '/home/your_username/.ssh/config', # Path to the SSH client config file
  line   => 'IdentityFile ~/.ssh/school', # Set the identity file
  match  => '^#?IdentityFile', # Match the line regardless of comments
}
