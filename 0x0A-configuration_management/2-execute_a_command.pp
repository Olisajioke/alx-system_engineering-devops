# Module: Ensure the 'killmenow' process is terminated
exec { 'killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
