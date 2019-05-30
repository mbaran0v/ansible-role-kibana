
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_conf_dir(host):
    f = host.file('/etc/kibana')

    assert f.exists
    assert f.is_directory


def test_config_file(host):
    f = host.file('/etc/kibana/kibana.yml')

    assert f.exists
    assert f.user == 'kibana'
    assert f.group == 'kibana'


def test_service(host):
    s = host.service('kibana')

    assert s.is_enabled
    assert s.is_running


def test_user(host):
    u = host.user('kibana')

    assert u.exists


def test_group(host):
    g = host.user('kibana')

    assert g.exists
