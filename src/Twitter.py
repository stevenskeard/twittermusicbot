#!/usr/bin/env python
import time
from threading import Thread

from SocketSender import SocketSender


class Twitter(Thread):
    # Class Attributes
    send_socket = None

    # Initializer / Instance Attributes
    def __init__(self, send_address):
        Thread.__init__(self)
        self.send_socket = SocketSender(send_address)

    def run(self):
        while True:
            try:
                print("Twitter")
                time.sleep(5)
            except KeyboardInterrupt:
                raise KeyboardInterrupt

    def stop(self):
        pass
