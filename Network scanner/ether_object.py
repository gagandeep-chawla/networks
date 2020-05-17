from scapy import all as scapy 

def main():
    erp_request = scapy.ARP(pdst = '10.0.2.1/24')
    '''
    now we are going to set the broadcast objects
    now using the Ether class of scapy
    '''
    broadcast = scapy.Ether()
    #now for checking the attributes we are going to use
    #scapy.ls method on this conditon please make pass the object not class
    print(broadcast.show())
    #show gives more details then summary method
    scapy.ls(scapy.Ether())
    '''
    'ff:ff:ff:ff:ff:ff' is the default value for the dst and its means its 
    request to the all the client
    dst        : DestMACField                        = 'ff:ff:ff:ff:ff:ff' (None)
    src        : SourceMACField                      = '08:00:27:74:d8:bc' (None)
    type       : XShortEnumField                     = 36864           (36864)
    '''
    '''
    now we are going to combining the both ARP and broadcast objects by 
    using the slash  /  
    ''' 
    arp_request_broadcast = broadcast/erp_request
    arp_request_broadcast.show()
    
    print(arp_request_broadcast.summary())
    #output of the return command say's its that return 
    #its will send broadcast to the other clients on the
    #network and return to 10.0.2.15 (my ip)
    #Ether / ARP who has Net('10.0.2.1/24') says 10.0.2.15

if __name__ == "__main__":
    main()