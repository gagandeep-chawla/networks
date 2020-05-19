from scapy import all as scapy
import argparse
'''
On this script we are going use the argparse because optparser
is depracted on python3 ,so on python3 argparse are used
and optparse are not longer provided
'''

class Parser:
    
    option = argparse.ArgumentParser()
    option.add_argument('-i','--IPAddress',dest = 'ip',
    help = 'User -i or --IPAddress for ip address')
    
    def __init__(self):
        self.parser = Parser.option.parse_args()

class Scan:

    def __init__(self,arp_instance):
        self.arp_instance = scapy.ARP(pdst = arp_instance)
        self.broadcast = scapy.Ether()
        self.arp_broadcast_instance = self.broadcast/self.arp_instance

    def scan(self):
        return scapy.srp(self.arp_broadcast_instance,timeout = 1)[0]

    def packets(self):
        packet_lists = self.scan()
        print('IP\t\t\tMac Address')
        for packet in packet_lists:
            print(packet[1].psrc+'\t\t\t'+packet[1].hwsrc)

def main():
    parser = Parser()
    scan = Scan(parser.parser.ip)
    scan.packets()

if __name__ == "__main__":
    main()