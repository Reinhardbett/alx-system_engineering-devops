## 0x0B.SSH
- The project will require one to establish an ssh connection using an RSA key instead of a password.
- The server used will be configured with a previously created public key
- One should use the IP and username  of their configured servers to connect via SSH

# General requirements
- All files will be interpreted on Ubuntu 20.04 LTS
- All Bash script files must be executable
- The first line of all Bash scripts should be ```#!/usr/bin/env bash```

# Task Nuggets
- The ssh program receives configuration (in order of importance) from the command line, the user-specific configuration file ~/.ssh/config and /etc/ssh/ssh_config
- When a user has created more than one SSH key for authentication, the -i command line option helps specify the key to use
- In the configuration files it may be specified in IdentityFile options.
- By specifying the private key in the IdentityFile options of our SSH client configuration file, we can connect without typing password:
# Without configuration
```
ssh -i ~/.ssh/school ubuntu@98.98.98.98
```
# With configuration
```
ssh ubuntu@98.98.98.98
```
