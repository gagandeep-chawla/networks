'''
In this file we have are going to scarpy from getting 
mac address of the router
'''
from scapy import all as scapy

def main():
    '''
    this methods returns the mac address of 
    the ip and this function also return
    range like if i want to find scan
    IP of all the range of subnet mask
    then like I have use like 10.0.01/24
    here /24 its mean 254 and so its will
    scan the the subnet mask till the 254
    '''
    #for the single subnet mask
    scapy.arping('10.0.2.1')
    #for the multiple subnet masks
    scapy.arping('10.0.2.1/24')



if __name__ == "__main__":
    main()