from fabric.api import env
import os

host1 = 'root@192.168.30.48'
host2 = 'root@192.168.30.51'
host3 = 'root@192.168.30.52'
host4 = 'root@192.168.30.49'
host5 = 'root@192.168.30.50'

ext_routers = [('blr-mx2','192.168.40.245')]
router_asn = 64512
public_vn_rtgt = 150
public_vn_subnet = '10.204.220.232/29'

host_build = 'stack@10.204.216.49'

env.test = {
    #'ci_flavor' :  'm1.medium'
    'ci_flavor' :  'contrail_flavor_medium'
}

env.roledefs = {
    'all': [host1, host2, host3, host4, host5],
    'contrail-controller': [host1,host4,host5],
    'openstack': [host1,host4,host5],
    'contrail-analytics': [host1,host4,host5],
    #'contrail-lb': [host4],
    'contrail-compute': [host2,host3],
    'contrail-analyticsdb': [host1,host4,host5],
    'build': [host_build],
}

if os.getenv('AUTH_PROTOCOL',None) == 'https':
    env.log_scenario='Multi-Interface Container Contrail HA Sanity[mgmt, ctrl=data, SSL]'
    env.keystone = {
        'auth_protocol': 'https'
    }
    env.cfgm = {
        'auth_protocol': 'https'
    }
else:
    env.log_scenario='Multi-Interface Container Contrail HA Sanity[mgmt, ctrl=data]'

if os.getenv('ENABLE_RBAC',None) == 'true':
    cloud_admin_role = 'admin'
    aaa_mode = 'rbac'
env.hostnames = {
    'all': ['nodea29', 'nodei8', 'nodem35', 'nodec60', 'nodek8']
}
env.physical_routers={
'blr-mx2'     : {       'vendor': 'juniper',
                     'model' : 'mx',
                     'asn'   : '64512',
                     'name'  : 'blr-mx2',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.216.245',
             }
}

env.kernel_upgrade=False
env.openstack = {
    'manage_amqp': "true"
}

env.keystone = {
    'keystone_ip': '192.168.30.90',
    'admin_password': 'c0ntrail123'
}

env.openstack_admin_password = 'c0ntrail123'
env.password = 'c0ntrail123'
env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    host_build: 'stack@123',
}

env.ostypes = {
    host1:'ubuntu',
    host2:'ubuntu',
    host3:'ubuntu',
    host4:'ubuntu',
    host5:'ubuntu',
}

control_data = {
    host1 : { 'ip': '192.168.40.48/24', 'gw' : '192.168.40.254', 'device':'enp94s0f0' },
    host2 : { 'ip': '192.168.40.51/24', 'gw' : '192.168.40.254', 'device':'nfp_p0' },
    host3 : { 'ip': '192.168.40.52/24', 'gw' : '192.168.40.254', 'device':'nfp_p0' },
    host4 : { 'ip': '192.168.40.49/24', 'gw' : '192.168.40.254', 'device':'enp1s0f1' },
    host5 : { 'ip': '192.168.40.50/24', 'gw' : '192.168.40.254', 'device':'ens1f0' },
    #host7 : { 'ip': '192.168.192.3/24', 'gw' : '192.168.192.254', 'device':'p6p2', 'vlan': '128' }
}
#env.ha = {
#    'contrail_internal_vip' : '192.168.192.4',
#    'contrail_external_vip' : '10.204.217.76'
#}
#ha_setup = True


env.cluster_id='clusterc7c8g36i1i2i3'
minimum_diskGB=32
env.test_repo_dir='/home/stack/multi_interface_parallel/ubuntu-14.04/icehouse/contrail-test'
env.rsyslog_params = {'port':19876, 'proto':'tcp', 'collector':'dynamic', 'status':'enable'}
env.mail_from='contrail-build@juniper.net'
env.mail_to='dl-contrail-sw@juniper.net'
multi_tenancy=True
env.interface_rename = True
env.encap_priority =  "VXLAN,MPLSoUDP,MPLSoGRE"
env.enable_lbaas = True
do_parallel = True
