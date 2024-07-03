# Puppet manifest used to manage SSH client configurations

file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('/alx-system_engineering-devops/my_module/ssh_config.erb'),
}
