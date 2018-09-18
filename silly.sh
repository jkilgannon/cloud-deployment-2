#!/bin/bash

echo "Test to see if the node is up by trying to hit the webserver."
sudo yum update
sudo yum install -y httpd
sudo systemctl restart httpd.service
