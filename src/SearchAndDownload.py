#!/usr/bin/env python
import socket
import time
from threading import Thread
from SocketReceiver import SocketReceiver
from SocketSender import SocketSender

class SearchAndDownload(Thread):

    # Class Attributes
    recvSocket = None
    sendSocket = None

    # Initializer / Instance Attributes
    def __init__(self, recvAddress, sendAddress):
        Thread.__init__(self)
        recvSocket = SocketReceiver(recvAddress)
        sendSocket = SocketSender(sendAddress)

    def run(self):
        while True:
            try:
                print("SearchAndDownload")
                time.sleep(5)
            except KeyboardInterrupt:
                raise KeyboardInterrupt

    def stop(self):
        pass
