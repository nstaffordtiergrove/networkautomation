#Nicholas Stafford 

from netmiko import ConnectHandler
from getpass import getpass

#Array for looping through multiple switches/routers

testIP = ['']

#Variable declaration for getpass

password = getpass()
print()

#Variable declarations for list of commands (This changes based on module)

command0 = "show run | i hostname"
command1 = "show run | i authorized"

#For loop to iterate through IP list

for x in testIP:
	
	device = {
	"device_type": "hp_procurve",
	"host": x,
	"username": "",
	"password": password,
	}
	
	command = ConnectHandler(**device)
	output0 = command.send_command(command0)
	output1 = command.send_command(command1)
	print(output0)
	print()
	print(output1)
	print()

#Next step is to output this to a file
