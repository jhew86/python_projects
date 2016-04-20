"""
TCP full-connect port scanner
"""
#step 1  input hostname, list of ports to scan
#step 2 translate hostname into ipv4 address
#step 3 for each port on list, connect to each port and target address
#step 4 determine specific service running on the port by sending \
#garbage data and reviewing the banner results that are returned.


import optparse #parses command=line arguments
import socket
from socket import* #creates network sockets

#translate hostname into ipv4 address
def connscan(tgtHost, tgtPort):#takes tgtHost & tgtPort args and attempts to connect
    try:
        connSkt=socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('violentpython\r\n')
        results=connSkt.recv(100)
        print('[+]%d/tcp open'% tgtPort)
        print('[+]' + str(results))
        connSkt.close()
    except:
        print('[-]%d/tcp closed', tgtPort)

def portscan(tgtHost, tgtPorts): #attempts to resolve hostname/ip_address
              try:
                  tgtIP= gethostbyname(tgtHost)
              except:
                  print("[-] cannot resolve '%s': unknown host" %tgtHost)
                  return
              try:
                  tgtName=gethostbyaddr(tgtIP)
                  print('\n[+] scan results for: ' + tgtName[0])
              except:
                  print('\n[+] scan results for: ' + tgtIP)
              setdefulttimeout(1)
              for tgtPort in tgtPorts:
                  print('scanning port ' + tgtPort)
              connscan(tgtHost, int(tgtPort))#initiats connscan function \n
              # to connect to detected ports

#application banner grabbing
def main():
              parser= optparse.OptionParser('usage %prog -H' +\
                              '<target host -p <target port>')
              parser.add_option('-H', dest='tgtHost', type='string', \
                  help='specify target host')
              parser.add_option('-p', dest= 'tgtPort', type='int', \
                  help='specify target port')
              (options, args) = parser.parse_args()
              tgtHost=options.tgtHost
              tgtPorts=str(options.tgtPort).split(' , ')
              if(tgtHost==None)|(tgtPorts==None):
                   print('[-] you must specify a target host and port[s]')
              portScan(tgtHost, tgtPorts)
exit(0)
if __name__ =='__main__':
              main()

#threading the scan
