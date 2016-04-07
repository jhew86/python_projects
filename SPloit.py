from socket import *
import sys, time

host=''
max_port = 5000
min_port = 1

try:
    host= input("[*]Enter target host address: ")
except KeyboardInterrupt:
        print("\n\n[*]User requested an interrupt")
        print("[*]Application shutting down")
        sys.exit(1)
hostip = gethostbyname(host)
for port in range(min_port,max_port):
    try:
        response = scan_host(host, port)
        if response ==0:
            print("[*]Port %d: open" % (port))
    except Exception as e:
            pass
    def scan_host(host, port, r_code = 1):
        try:
            s=socket(AF_INET, SOCK_STREAM)
            code = s.connect_ex(host, port)
            if code==0:
                r_code=code
            s.close()
        except Exception as e:
            pass
        return r_code
