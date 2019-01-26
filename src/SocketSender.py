#!/usr/bin/env python
import socket

class SocketSender:

    # Class Attributes
    address = None
    maxMessageSize = 1024

    # Initializer / Instance Attributes
    def __init__(self, _address):
        address = _address

    def sendMessage(self, message):
        while True:
            try:
                s = socket.socket(SOCKET.AF_UNIX, socket.SOCK_STREAM)
                s.connect(address)
                s.send(message)
                s.close()
            except:
                pass
            finally:
                s.close()
