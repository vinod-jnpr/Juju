Enable root login on the controller and compute nodes(in our case a29-Controller and i8,m35 compute nodes)

Export the below environment values and modify AUTH_URL ip, it should be the keystone ip address

```
export OS_IDENTITY_API_VERSION=3
export OS_AUTH_URL=http://192.168.11.24:5000/v3
export OS_USER_DOMAIN_NAME=admin_domain
export OS_USERNAME=admin
export OS_PASSWORD=c0ntrail123
export OS_PROJECT_DOMAIN_NAME=admin_domain
export OS_PROJECT_NAME=admin
export OS_DOMAIN_NAME=admin_domain
```

Use the contrail_test_input.yaml sample and modify the ip of the nodes 

```
192.168.21.5 is the data interface ip of nodea29
192.168.11.24 is the keystone ip
10.204.217.158 is the local DNS ip
```

Run the script below and ensure it works

```
PYTHONPATH=./scripts:./fixtures TEST_CONFIG_FILE=contrail_test_input.yaml python -m testtools.run scripts.vm_regression.test_vm_basic.TestBasicVMVN.test_ping_within_vn_two_vms_two_different_subnets
```

# yaml file of Ankit

```
https://github.com/Juniper/contrail-tools/commit/81a2fa185c2cbe0a38fb78cfa0b518902e8b8ff8
```

# Bundle file of Anikit

```
https://github.com/nuthanc/nuthanc-nodem4/blob/master/d2_configs/bundle_netronome.yaml
```

