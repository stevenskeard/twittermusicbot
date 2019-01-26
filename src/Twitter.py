#!/usr/bin/env python
import socket
from threading import Thread
from SocketSender import SocketSender

class Twitter(Thread):

    # Class Attributes
    sendSocket = None

    # Initializer / Instance Attributes
    def __init__(self, sendAddress):
        Thread.__init__(self)
        sendSocket = SocketSender(sendAddress)

    def run(self):
        while True:
            try:
                print ("Twitter")
            except KeyboardInterrupt:
                raise KeyboardInterrupt
    def stop(self):
        pass
