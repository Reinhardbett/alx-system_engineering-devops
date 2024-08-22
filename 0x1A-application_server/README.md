## 0x1A. Application server

# Requirements
Everything Python-related must be done using python3
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

# Setting up server
echo "Updating Packages and Installing Requirements"

# Update Package Manager
sudo apt-get update
sudo apt-get install -y nginx
# Install pip
sudo apt-get install -y python3-pip
# Install Flask, flask_cors, sqlalchemy Using PIP
pip install flask
pip install flask_cors
pip install sqlalchemy
# Install net-tools
sudo apt install -y net-tools
# Install GUNICORN
sudo apt-get install -y gunicorn
