import subprocess
import re

'''
on this file we going to retrieve current mac extres via using the check_output 
of the subprocess method
'''
#this method are take list attributes
config_instance = subprocess.check_output(['ifconfig'])
print(f'The value of the ifconfig -{config_instance}')
#for python3 we have used the decode method
mac_address = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',config_instance.decode())
print(f'The Value of the mac_Address -{mac_address.group(0)}')