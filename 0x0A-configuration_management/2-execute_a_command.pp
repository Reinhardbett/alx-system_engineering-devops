# This Puppet manifest kills a process named "killmenow"

exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/bin/pgrep killmenow',
}
