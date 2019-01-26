#!/usr/bin/env python
import socket
import time
from threading import Thread
from SocketReceiver import SocketReceiver

class AudioPlayer(Thread):

    # Class Attributes
    recvSocket = None

    # Initializer / Instance Attributes
    def __init__(self, address):
        Thread.__init__(self)
        recvSocket = SocketReceiver(address)

    def run(self):
        while True:
            try:
                print("AudioPlayer")
                time.sleep(5)
            except KeyboardInterrupt:
                raise KeyboardInterrupt

    def stop(self):
        pass
