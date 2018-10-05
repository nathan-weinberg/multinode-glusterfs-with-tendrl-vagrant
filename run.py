import os
import yaml
import getpass

config = {}

print('Hit "Crtl-C" to exit at any time.')

# Select bootstrap
while True:
	setupType = input('Do you want an upstream or downstream setup? (type "upstream" or "downstream") ').lower()
	if setupType == "upstream":
		config["bootstrap"] = "bootstrap_upstream.sh"
		break
	elif setupType == "downstream":
		config["bootstrap"] = "bootstrap_downstream.sh"
		break
	else:
		print("Invalid option.")

# Select number of nodes
while True:
	nodeQuantity = int(input('How many storage nodes would you like in your setup? (type number) '))
	if nodeQuantity < 1:
		print("Invalid option.")
	else:
		config["storage_node_count"] = nodeQuantity
		break

# Specify NTP server
ntpServer = input("Please specify your NTP server: ")
config["ntp_server"] = ntpServer

# Specify RHEL credentials if setup is downstream
if setupType == "downstream":
	username = input("Please input your RHEL username: ")
	password = getpass.getpass("Please input your RHEL password (password will not be shown): ")
	config['rhel_username'] = username
	config['rhel_password'] = password

# write config to YAML file
file = open('conf.yml', 'w')
yaml.dump(config, file)
file.close()

# execute vagrant up
os.system("vagrant up")

# erase credentials from YAML file after `vagrant up` completes
config['rhel_username'] = ""
config['rhel_password'] = ""
file = open('conf.yml', 'w')
yaml.dump(config, file)
file.close()
