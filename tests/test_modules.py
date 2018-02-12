import pytest
import re


@pytest.fixture()
def AnsibleDefaults(Ansible):
    """ Load default variables into dictionary.
    Args:
        Ansible - Requires the ansible connection backend.
    """
    return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


def test_modules(AnsibleDefaults, PipPackage):
    """ Ensure urllib3 is installed.

    Args:
        GetAnsibleDefaults - Get default version of the package
        PipPackage - Get all installed pip packages
    """
    installed_pkgs = PipPackage.get_packages()

    # Get package version from Ansible variables.
    pkg_version = re.match("\d+\.\d+",
        AnsibleDefaults["python_security_urllib3_version"].split("*")[0]).group(0)  # NOQA E501

    assert 'urllib3' in installed_pkgs.keys()
    assert pkg_version in installed_pkgs["urllib3"]["version"]


def test_python_ssl(Ansible, File):
    """ Ensure Python TLS SNI is working

    Args:
        Ansible -  Use get_url to download a file from a host known to have
                   TLS SNI enabled.
        File - Check to see if file downloaded with get_url exists.
    """
    get_docker_key = Ansible('get_url',
                             'url=https://download.docker.com/linux/ubuntu/gpg\
                             dest=/tmp/docker.key',
                             check=False)
    assert get_docker_key["status_code"] == 200
    assert File("/tmp/docker.key").exists
