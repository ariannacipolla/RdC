#!/usr/bin/env python

# Saverio Mattia Merenda 08/11/2023

import sys, signal, os
#import select
import optparse
from socket import *

parser = optparse.OptionParser()
parser.add_option('-p', '--port',     dest="port", default=9056,  type=int  )
parser.add_option('-s', '--server',   dest="server", default="172.17.0.3", )
parser.add_option('-b', '--bufsize',  dest="bufsize", default=1024,  type=int , help="dimensione buffer" )
options, remainder = parser.parse_args()

print ("   port:", options.port, "  server:", options.server, "bufsize:",options.bufsize)

s = socket(AF_INET,SOCK_DGRAM)
s.bind((options.server,options.port))

while(1):
        data,addr = s.recvfrom(options.bufsize)
        print ("addr:",addr," data:", data.decode())

