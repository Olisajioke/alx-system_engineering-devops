#  A scrip that atttempts to change the OS configuration so that it is possible to login with a
# specifier user like the holberton user and open a file without displaying any error messages to the console.

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
