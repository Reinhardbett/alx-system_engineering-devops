## Configuration Management
- This project will work with the configuration management system**puppet**
- The Puppet manifests are verified with puppet-lint version 2.1.1
- Each Puppet manifest will contain a comment explaining what the Puppet manifest is about

## Requirements
- Ubuntu 20.04 VM should have Puppet 5.5 preinstalled
- Install *puppet*
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
- Install *puppet-lint*
```
$ gem install puppet-lint
```
