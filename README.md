# Ansible role: Kibana

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-kibana.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-kibana)

**THIS ROLE IS FOR 6.x, 5.x.**

Ansible role for 6.x/5.x Kibana. Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* Ubuntu 14.04
* Debian 9
* Debian 8
* CentOS 7
* CentOS 6

Requirements
------------

None.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
# kibana version
kibana_major_version: "6.x"
kibana_version: "6.3.0"

# kibana config for listen address and port
kibana_config_server:
  server.port: 5601
  server.host: "localhost"
  # server.basePath: ""
  server.maxPayloadBytes: 1048576
  # server.name: "your-hostname"

# kibana config for ES address
kibana_config_es:
  elasticsearch.url: "http://localhost:9200"
  elasticsearch.preserveHost: true
  elasticsearch.requestTimeout: 30000

```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: kibana
      roles:
         - { role: mbaran0v.kibana }

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
