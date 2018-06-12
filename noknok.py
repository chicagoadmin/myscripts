#!/usr/bin/env python 

# ye old port knock and check 
# nothing fancy 


import itertools
import socket
from time import sleep 

ip = '10.10.10.8'
ports = (8890, 7000, 666)
wanted = 31337

def getallcombos(plist):
    allcombos = [] 
    for seq in list(itertools.permutations(plist,r=None)):
        allcombos.append(seq)
    return allcombos

def knockknock(combo, knocked):
    for p in combo:
#      sleep(2)
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print "Connecting to %s..." % p
      try:
          s.connect((ip, p))
      except:
          pass
    m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    m.settimeout(0.1)
    try:
        print "Connecting to knocked port %s" % knocked 
        m.connect((ip,knocked))
        data = m.recv(1024)
        print list(data)
    except:
        pass
    s.close

#print list(getallcombos(ports))

for combo in getallcombos(ports):
    knockknock(combo, wanted)
#    response = raw_input("Do you want to continue knocking [Y/n]")
#    if response.upper() == 'N':
#        exit(0)
#    else:
#        next
#    sleep(5)

