# Execuet the above commands with root login

1. Untar contrail-cloud-docker_4.1.1.0-<build>-ocata_xenial.tgz (get this from support site) and get contrail-dockers:
- #tar -xvf contrail-cloud-docker_4.1.1.0-<build>-ocata_xenial.tgz

 
2. Setup local repo:
- #apt install -y gnupg dpkg-sig rng-tools reprepro
- #gpg --gen-key
- #gpg --armor --output packages.linux-admins.key --export
- #apt-get install apache2
- ## Extract Contrail packages in /var/www/html
- #mv contrail-networking-docker_4.1.1.0-<build>_xenial.tgz /var/www/html/.
- #cd /var/www/html/
- #tar -xzf contrail-networking-docker_4.1.1.0-<build>_xenial.tgz;
- #rm contrail-networking-docker_4.1.1.0-<build>_xenial.tgz
- #for i in $(ls *.tgz); do tar -xzf $i; rm $i; done
 
- ##Add Netronome packages in /var/www/html
- #cd /var/www/html/
- #tar -xvf Netronome_R4.1.2_build_<build_nr>_Juju.tar
- #cp Netronome_R4.1.2_build_<build_nr>_Juju/debs/netronome-debs/*.deb .
- #apt-get -y install docker.io docker
 
- ## Add patched openstack packages in /var/www/html
- #cd Netronome_R4.1.2_build_<build_nr>_Juju/debs/package_builder
- #./create-opentack-packages.sh
- #cd /var/www/html/
- #cp Netronome_R4.1.2_build_<build_nr>_Juju/debs/package_builder/patched-openstack-packages/*.deb .
- #rm -r Netronome_R4.1.2_build_<build_nr>_Juju       

- #cd /var/www/html/
- #mkdir -p ubuntu/conf
- #cd ubuntu/conf

#cat <<EOF > distributions
Origin: contrail.juniper.net
Label: contrail.juniper.net
Codename: xenial
Architectures: amd64 source
Components: main
Description: Contrail 4.1 Repository
SignWith: yes
DebOverride: override.xenial
DscOverride: override.xenial
EOF
#cat <<EOF > options
verbose
ask-passphrase
basedir /var/www/html/ubuntu
EOF
- #touch override.xenial
- #cd /var/www/html/ubuntu
- #reprepro --ask-passphrase -Vb . includedeb xenial /var/www/html/*.deb
 
