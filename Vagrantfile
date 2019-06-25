# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
  
  config.vm.define "service" do |service|

    service.vm.box = "ubuntu/bionic64"
    service.vm.network "forwarded_port", guest: 9000, host: 9001
    #service.vm.network "public_network", bridge: "ens3"
    service.vm.network "private_network", ip: "192.168.33.10"
    service.vm.hostname = "service"

    service.vm.provider "virtualbox" do |vb|
            vb.memory = "2048"
            vb.name = "service"
    end

  end

  config.vm.define "monitoring" do |monitoring|

    monitoring.vm.box = "ubuntu/bionic64"
    #monitoring.vm.network "public_network"
    monitoring.vm.network "private_network", ip: "192.168.33.11"
    monitoring.vm.hostname = "monitoring"

    monitoring.vm.provider "virtualbox" do |vb|
            vb.memory = "2048"
            vb.name = "monitoring"
    end

  end

  config.vm.provision "shell", inline: <<-SHELL
        echo "Installing Docker"
        sudo apt update
        sudo apt upgrade
        sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo apt-key fingerprint 0EBFCD88
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
        sudo apt update
        sudo apt -y install docker-ce docker-ce-cli containerd.io
        sudo usermod -aG docker $USER
        sudo systemctl start docker
        git clone https://github.com/carolineap/tarsd-final.git
  SHELL

end
