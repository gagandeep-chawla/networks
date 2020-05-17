'''
In this method we are going to the send packets via broadcast and arp
intances
'''
from scapy import all as scapy

def main():
    arp_instance = scapy.ARP(pdst = '10.0.2.1/24')
    broadcast = scapy.Ether()
    arp_broadcast_instance = broadcast/arp_instance 
    '''
    now we are calling the srp stands for send and receive protocal
    this methods is similarly to the sr but here we are using the
    custom boardcast as per the doc so we have use the srp and timeout 
    artribute else its will no stop,
    this method return two list i.e packets which answered and packets
    which don't answered.
    '''
    answered,unanswered = scapy.srp(arp_broadcast_instance,timeout = 1)
    print('answered.summary()')
    print(answered.summary())
    print('------------------------')
    # print('unanswered.summary()')
    # print(unanswered.summary())

if __name__ == "__main__":
    main()