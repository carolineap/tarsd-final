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
            vb.memory = "4096"
            vb.name = "service"
    end

    service.vm.provision "shell" do |s|
        s.inline = "sudo apt update"
        s.inline = "sudo apt -y upgrade"
        s.inline = "sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common"
        s.inline = "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
        s.inline = "sudo apt-key fingerprint 0EBFCD88"
        s.inline = "sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'"
        s.inline = "sudo apt update"
        s.inline = "sudo apt -y install docker-ce docker-ce-cli containerd.io"
        s.inline = "sudo systemctl start docker"
        s.inline = "sudo systemctl enable docker"
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
    
    monitoring.vm.provision "shell" do |s|
        s.inline = "sudo apt update"
        s.inline = "sudo apt -y upgrade"
        s.inline = "sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common"
        s.inline = "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
        s.inline = "sudo apt-key fingerprint 0EBFCD88"
        s.inline = "sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'"
        s.inline = "sudo apt update"
        s.inline = "sudo apt -y install docker-ce docker-ce-cli containerd.io"
        s.inline = "sudo systemctl start docker"
        s.inline = "sudo systemctl enable docker"
    end

  end

end
