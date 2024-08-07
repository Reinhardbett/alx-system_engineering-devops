# installing nginx with puppet

package {'nginx':
  ensure => 'present',
}

exec {'installation of puppet':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'echoing hello would into index.html':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'using sed for redirection':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/blog.ehoneahobed.com\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
