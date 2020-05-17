import subprocess
import optparse
'''
optparser works as like sys.argv its retrieves the argument 
from when we run the script.
'''
def excaute_optparser():
    option = optparse.OptionParser()
    
    '''
    on the add_option method args argument to define which permerter
    they are accepting like python optparser.py -i eth0 -m 01:02:03:04:05:06
    and dest is the key of those to retrieve the data
    '''

    option.add_option('-i','--interface',
    dest = 'interface',help = 'please choose the interface for changing the mac address')
    option.add_option('-m','--mac',dest = 'mac',
    help = 'Add new mac address')
    #parse_get retrieve the data from the passed argument 
    (option, _) = option.parse_args()
    return (option.interface, option.mac)



def excaute_subprocess(command):
    try:
        #this is not sceure 
        if isinstance(command,str):
            subprocess.call(command,shell=True)

        if isinstance(command,list):
            subprocess.call(command)

    except Exception as e:
        raise e


def main():
    interface,mac_address = excaute_optparser()
    # print(subprocess.call('ifconfig'))
    excaute_subprocess('sudo ifconfig {} down'.format(interface))
    excaute_subprocess('sudo ifconfig {} hw ether {}'.format(interface, mac_address))
    excaute_subprocess('sudo ifconfig {} up'.format(interface))
    # print(subprocess.call('ifconfig'))
    # excaute_subprocess(['sudo','ifconfig',interface,'down'])
    # excaute_subprocess(['sudo','ifconfig',interface,'hw','ether',mac_address])
    # excaute_subprocess(['sudo','ifconfig',interface,'up'])
    # excaute_subprocess('ifconfig')
    # remaining things python optparser_option.py -i eth0 -m 00:11:22:33:44:55tomorrow
if __name__ == "__main__":
    main()

'''
how to run the scirpt  
python optparser_option.py -i eth0 -m 00:11:22:33:44:55
'''