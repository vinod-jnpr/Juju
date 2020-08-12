# Setting up reverse SSH

On noded2(10.204.216.57) modify /etc/ssh/sshd_config

```
GatewayPorts clientspecified
```

do a restart of sshd

```
service sshd restart
```


Command for login to openstack-dashboard

```
juju ssh openstack-dashboard/0 
```

Create a reverse SSH tunnel inoder to view the horizon .

The  below command should be run on openstack-dashboard.
It connects openstack-daskboard to noded2(192.168.11.2)


```
ssh -fN -R 0.0.0.0:9999:localhost:80 root@192.168.30.9
```

# To view the horizon UI

The horizon page van be viewed by the below commands, (10.204.216.57) below is ip of noded2 port(9999) is port used for reverse SSH

```
http://10.204.216.219:9999/horizon
```

# To launch Vm's and ping between them

```
The Vm's can be created using the above UI
Once created, Please check the compute nodes in which they have be created
Login in to the compute and from there to the VM's using (ubuntu/ubuntu)
Ping from there to the other Vm's and check the connectivity
```
