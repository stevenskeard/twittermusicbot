#!/usr/bin/env python
import socket,os
from threading import threading.Thread
from .SocketSender import SocketSender

class SearchAndDownload:

    # Class Attributes
    sendSocket = null

    # Initializer / Instance Attributes
    def __init__(self, recvAddress, sendAddress):
        sendSocket = SocketSender("Twitter", sendAddress)

    def run(self):
        #Temp - exit
        raise SystemExit
