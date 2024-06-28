# install flask from pip3 version 2.1.0

# ensure pip is installed
exec { 'install_pip':
  command => '/usr/bin/python3 -m ensurepip --upgrade',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/pip3 --version',
}

#Ensure Flask version 2.1.0 is installed
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Exec['install_pip'],
}
