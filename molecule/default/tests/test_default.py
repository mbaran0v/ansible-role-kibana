import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kibana_config(host):
    f = host.file('/etc/kibana/kibana.yml')

    assert f.exists
    assert f.user == 'kibana'
    assert f.group == 'kibana'
    # assert f.contains('elasticsearch.url: "http://127.0.0.1:9201"')


def test_kibana_socket(host):
    s = host.socket('tcp://127.0.0.1:5602')

    assert s.is_listening


def test_kibana_serice(host):
    s = host.service('kibana')

    assert s.is_enabled
    assert s.is_running
