#written on/for Mac OSX

import os
ip_list = ['8.8.8.8', '8.8.4.4', '192.168.1.1']

#the function 

def ping_ip(ip_address):
    response = os.system(f'ping -c 1 {ip_address}')
    if response == 0:
        print(f'{ip_address} is up.')
    else:
        print(f'{ip_address} is down.')

#gotta check those IPs

for ip in ip_list:
    ping_ip(ip)

#try it out! 