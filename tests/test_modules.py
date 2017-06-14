import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    """ Load default variables into dictionary.
    Args:
        Ansible - Requires the ansible connection backend.
    """
    return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


@pytest.mark.parametrize("pkg_name", [
    "pyasn1",
    "ndg-httpsclient",
])
def test_modules(AnsibleDefaults, PipPackage, pkg_name):
    """ Ensure pip modules are installed.

    Args:
        GetAnsibleDefaults - Get default version of the package
        PipPackage - Get all installed pip packages
    """
    installed_pkgs = PipPackage.get_packages()

    # Get package version from Ansible variables. Naming convention is
    # <package_name_without_hyphens>_version
    pkg_version = AnsibleDefaults[
        "python_security_{}_version".format(pkg_name.replace("-", ""))
    ].split("*")[0]

    assert pkg_name in installed_pkgs.keys()
    assert pkg_version in installed_pkgs[pkg_name]["version"]


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
