'''
In this file we have are going to scarpy from getting 
mac address of the router
'''
from scapy import all as scapy

def main():
    scapy.arping('10.0.2.1')


if __name__ == "__main__":
    main()