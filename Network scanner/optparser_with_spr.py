import optparse
from scapy import all as scapy
'''
In this script we are going to use the optparser for
taking ip via running the scirpt
'''

def parser_arguments():
    option = optparse.OptionParser()
    option.add_option('-i','--IPAddress',dest = 'ip',
    help = 'This field use for the IP address')
    (option, _)=option.parse_args()
    import pdb; pdb.set_trace()
    return option.ip

def main():
    arp_instance = scapy.ARP(pdst = str(parser_arguments()))
    broadcast = scapy.Ether()
    arp_broadcast_instance = broadcast/arp_instance
    #verbose removed the unrequired information and strings
    answered = scapy.srp(arp_broadcast_instance, timeout = 1)[0]
    print('IP\t\t\tMac Address\n--------------------------------------')
    for elements in answered:
        '''
        each elements contains contains an list of two elements
        first element is the packet that we are sending and 
        second element is the answered of the send packets
        '''
        # print(elements[1].show())
        #hwsrc is the mac address of destination
        #psrc is the ip address of destination
        print(elements[1].psrc+'\t\t\t'+elements[1].hwsrc)
        
if __name__ == "__main__":
    main()