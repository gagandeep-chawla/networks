import subprocess

def excaute_subprocess(command):
    try:
        #this is not sceure 
        if isinstance(command,str):
            subprocess.call(command,shell=True)
        
        '''
        here command followerd by the first element
        of list then if the second element have those 
        attribute then only this command are excaute 
        else it through error
        for example:-
        command[0] is ifconfig
        command[1] is ethO
        here is eth0 is found then only its will excaute 
        else i  t will not excaute
        '''
        if isinstance(command,list):
            subprocess.call(command)


    except Exception as e:
        raise e


def main():
    # print(subprocess.call('ifconfig'))
    # excaute_subprocess('sudo ifconfig eth0 down')
    # excaute_subprocess('sudo ifconfig eth0 hw ether 00:02:03:04:05:06')
    # excaute_subprocess('sudo ifconfig eth0 up')
    print(subprocess.call('ifconfig'))
    excaute_subprocess(['sudo','ifconfig','eth0','down'])
    excaute_subprocess(['sudo','ifconfig','eth0','hw','ether','00:11:22:33:44:55'])
    excaute_subprocess(['sudo','ifconfig','eth0','up'])
    excaute_subprocess('ifconfig')
    # remaining things tomorrow
if __name__ == "__main__":
    main()