# Puppet module to configure SSH client settings

$file_content = @(CONTENT)
Host *
        PasswordAuthentication no
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/school
        HostName 54.197.21.228
        User ubuntu
CONTENT

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => $file_content,
  mode    => '0600', 
}
