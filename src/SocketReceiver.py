#!/usr/bin/env python
import socket

class SocketReceiver:

    # Class Attributes
    address = None
    maxMessageSize = 1024

    # Initializer / Instance Attributes
    def __init__(self, _address):
        address = _address

    def getMessage(self):
        while True:
            try:
                s = socket.socket(SOCKET.AF_UNIX, socket.SOCK_STREAM)
                s.bind(address)
                s.listen(1)
                conn, addr = s.accept()
                while True:
                    data = conn.recv(maxMessageSize)
                    if not data: break
                    return data;
            except:
                pass
            finally:
                s.close()
