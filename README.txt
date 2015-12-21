Project: Catalog App  - Omar Hiari
================================

Required Libraries and Dependencies
-----------------------------------
Project requires Python v2.*, vargrant v1.7.4, and VirtualBox 5.0.10 to be installed


How to Run Project
------------------
Ensure that your Vagrant configuration file "Vagrantfile" contains the line "config.vm.network "forwarded_port", guest: 5000, host: 5000"
Then from command line do the following:
- Use the command "vagrant up" to power on the virtual machine 
- Use the command "vagrant ssh" to log into the virtual machine
- cd into /vagrant/catalog
- Execute the command "python database_setup.py"
- Execute the command "python catalogentries.py"
- Execute the command "python catalogapp.py"
- Open a web browser window and browse to "http://localhost:5000"
