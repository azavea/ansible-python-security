# ansible-python-security
Ansible Role to add Python support for TLS SNI.

## Role Variables

- `python_security_ndghttpsclient_version`: Version of `ndg-httpsclient` to install. (Default: `"0.4.*"`)
- `python_security_pyasn1_version`: Version of `pyasn1` to install. (Default: `"0.2.*"`)

## Testing
### Requirements
- Virtualbox 5.1.22+ 
- Vagrant 1.9.5+
- Pip 9.0.1+
- Molecule <= 1.25
- Ansible 2.3.1+

### Overview
Tests are done using [molecule](http://molecule.readthedocs.io/). To run the test suite, install molecule and its dependencies and run ` molecule test` from the folder containing molecule.yml. To add additional tests, add a [testinfra](http://testinfra.readthedocs.org/) python script in the [tests](./tests/) directory, or add a function to [test_modules.py](./tests/test_pip.py). Information about available Testinfra modules is available [here](http://testinfra.readthedocs.io/en/latest/modules.html).

### Example 
```
# Download molecule, dependencies
$ pip install molecule

# Change to the top-level project directory, which contains molecule.yml
$ cd /path/to/ansible-python-security

# Ensure that molecule.yml is present
$ ls
CHANGELOG.md 	molecule.yml
LICENSE 	README.md
playbook.yml 	tasks
defaults 	tests
meta 		roles.yml

# We're in the right directory, so let's run tests!
$ molecule test

