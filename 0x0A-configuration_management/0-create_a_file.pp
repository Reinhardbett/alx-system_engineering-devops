# create a file school with specific permissions, owner, group, and content

file { '/tmp/school':
  ensure  => 'file',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
