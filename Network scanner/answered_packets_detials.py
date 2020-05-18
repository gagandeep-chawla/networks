from scapy import all as scapy
'''
In this file we are going to iterated the answered packets list
'''

def main():
    arp_instance = scapy.ARP(pdst = '10.0.2.1/24')
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