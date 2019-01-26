#!/usr/bin/env python
import socket,os
from threading import threading.Thread
from .SocketReceiver import SocketReceiver
from .SocketSender import SocketSender

class SearchAndDownload:

    # Class Attributes
    recvSocket = null
    sendSocket = null

    # Initializer / Instance Attributes
    def __init__(self, recvAddress, sendAddress):
        recvSocket = SocketReceiver("SearchAndDownload", recvAddress)
        sendSocket = SocketSender("SearchAndDownload", sendAddress)

    def run(self):
        #Temp - exit
        raise SystemExit
