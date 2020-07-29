# Bringing up
wget https://github.com/tungstenfabric/tf-test/raw/master/testrunner.sh

testrunner.sh load docker-image-contrail-test-ocata-4.1.5.0-66.tar.gz

sudo ./testrunner.sh run -s contrail-test-ocata:4.1.5.0-66

copy testbed file to : /opt/contrail/utils/fabfile/testbeds/
& then python tools/configure.py -p /opt/contrail/utils/ ./


bash -x tools/check_test_discovery.sh > tests.txt

./testrunner.sh run -s -t <testbed.py> <contrail-test docker image> 
to bring up a new docker image

# Adding static route in neutron_api

add this in the controller
sudo route add -net 192.168.30.81<IP of neturon api>  netmask 255.255.255.255 gw 192.168.40.254

Inside neutron_api  : sudo ip route add 192.168.40.0/24 via 192.168.30.254

# Copy this file to test Container

/root/ankit/contrail-test/images/ubuntu.vmdk.gz
Present in nodem4 also

To enable Netronome : in sanity_testbed.json  , Enable flag "ns_agilio_vrouter": "True"


export PYTHONPATH=./scripts:./fixtures:./serial_scripts

python -m testtools.run scripts.vm_regression.test_vm_basic.TestBasicVMVN.test_vm_add_delete

