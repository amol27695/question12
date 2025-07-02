#!/usr/bin/env python3

import json

def generate_inventory():
    inventory = {
        "web": {
            "hosts": [
                "serverb.lab.example.com"
            ]
    },
    "_meta": {
        "hostvars": {
            "serverb.lab.example.com": {
                "ansible_host": "serverb.lab.example.com",
                "ansible_user": "root",
              }
       }
    }
}
    return inventory

if__name__ == "__main__":
   print(json.dumps(generate_inventory(), indent=2))
