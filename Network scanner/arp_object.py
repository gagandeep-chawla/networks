from scapy import all as scapy 

def main():
    obj = scapy.ARP()
    #let the print obj intance 
    print(obj.summary())
    #o/p :- ARP who has 0.0.0.0 says 10.0.2.15
    #0.0.0.0.0 is the IP
    '''
    now for we are checking the ip we to get which
    attribute we have to change for the on ARP object 
    '''
    # scapy.ls(scapy.ARP)
    #above command work just like the linux command
    #output of the above command
    '''
    hwtype     : XShortField                         = (1)
    ptype      : XShortEnumField                     = (2048)
    hwlen      : ByteField                           = (6)
    plen       : ByteField                           = (4)
    op         : ShortEnumField                      = (1)
    hwsrc      : ARPSourceMACField                   = (None)
    psrc       : SourceIPField                       = (None)
    hwdst      : MACField                            = ('00:00:00:00:00:00')
    pdst       : IPField                             = ('0.0.0.0')
    'my command' :- pdst is works as ip
    '''
    #now we are going to create object with pdst value then check the summary
    obj_2 = scapy.ARP(pdst = '10.0.2.1/24')
    #ouptput of above command ARP who has 10.0.2.1 says 10.0.2.15
    print(obj_2.summary())   

if __name__ == "__main__":
    main()