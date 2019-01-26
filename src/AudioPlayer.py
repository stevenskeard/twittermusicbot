#!/usr/bin/env python
import socket,os
from threading import threading.Thread
from .SocketReceiver import SocketReceiver

class AudioPlayer(Thread):

    # Class Attributes
    recvSocket = null

    # Initializer / Instance Attributes
    def __init__(self, address):
        super(self)
        address = _address
        recvSocket = SocketReceiver("AudioPlayer", address)

    def run(self):
        #Temp - exit
        raise SystemExit
