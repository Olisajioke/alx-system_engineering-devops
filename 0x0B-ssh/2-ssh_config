#!/usr/bin/env bash
# Configures the SSH client to use the private key ~/.ssh/school and refuse password authentication

cat <<EOF > ~/.ssh/config
Host *
  PasswordAuthentication no

Host target_server
  Hostname 98.98.98.98
  IdentityFile ~/.ssh/school
  User ubuntu
EOF
