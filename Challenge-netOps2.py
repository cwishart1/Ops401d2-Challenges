#!/usr/bin/env python3

# Script Name:                  Challenge-netOps2
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      4/22/21
# Purpose:                      Build a network scanning tool

# Import Lib
import random
from scapy.all import ICMP, IP, sr1, TCP
import ipaddress

# Define Var
x = input("(1) TCP Port Range Scanner\n(2) ICMP Ping Sweep\nEnter desired function (1-2): ")
port_range = [22, 23, 80, 443, 3389]

# Main
if x == '1':
    host = input("Enter IP to be scanned: ")
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        res = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='S'),timeout=1,verbose=0,)
        if res is None:
            print(f"{host}:{dst_port} was silently dropped.")
        elif(res.haslayer(TCP)):
            if(res.getlayer(TCP).flags == 0x12):
                sendRst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0,)
                print(f"{host}:{dst_port} is open.")
            elif(res.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed.")
        elif(res.haslayer(ICMP)):
            if(int(res.getlayer(ICMP).type) == 3 and int(res.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print(f"{host}:{dst_port} was silently filtered.")
elif x == '2':
    net = input("Enter in target network with CIDR block (x.x.x.x/24): ")
    count = 0
    block = 0
    scanned = 0
    ipList = ipaddress.ip_network(net)
    for host in ipList.hosts():
        print("Pinging",host,", please wait...")
        response = sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)
        if response is None:
            print (f"{host} is down")
            scanned+=1
        elif response.haslayer(ICMP):
            scanned+=1
            count+=1
            if (int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) [1,2,3,9,10,13]):
                block+=1
                print (f"{host} blocks ICMP traffic")
            else:
                print(f"{host} is up. Hosts online: {count}")
    print (f"""{scanned} ip addresses scanned. {count} hosts are up; {block} are blocking ICMP traffic.""") 
    
    # End
