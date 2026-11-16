from netmiko import ConnectHandler
from getpass import getpass

testIP = [ ""] # Insert IP's here you want to SSH into

username = input('What is your RADIUS username: ')

password = getpass()

command1 = "show ip int br | i vlan" # Example command

for x in testIP:
	
	device = {
	"device_type": "cisco_ios", # cisco_ios replaced with whatever vendor you are working with
	"host": x,
	"username": username,
	"password": password,
}
	with ConnectHandler(**device) as connect:
		output1 = connect.send_command(command1)
		print(output1)

