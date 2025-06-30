#!/bin/bash

chmod +x inventory.py

ansible-navigator run main.yml -i inventory.py --eei hub.lab.example.com/ansible-builder-rhel8:latest --pae false --pp missing -m stdout
