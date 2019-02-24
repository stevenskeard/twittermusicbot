#!/usr/bin/env python
from threading import Thread
from subprocess import call

from SocketReceiver import SocketReceiver

class AudioPlayer(Thread):
    # Class Attributes
    receive_socket = None
    video_dir = None

    # Initializer / Instance Attributes
    def __init__(self, address, video_dir):
        Thread.__init__(self)
        self.receive_socket = SocketReceiver(address)
        self.video_dir = video_dir

    def run(self):
        while True:
            try:
                next_video = self.receive_socket.getMessage()
                call("mpg123 " + self.video_dir + "/" + next_video, shell=True)
            except KeyboardInterrupt:
                raise KeyboardInterrupt

def stop(self):
    pass
