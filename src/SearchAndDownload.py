#!/usr/bin/env python
from subprocess import call
from threading import Thread

from SocketReceiver import SocketReceiver
from SocketSender import SocketSender


class SearchAndDownload(Thread):
    # Class Attributes
    receive_socket = None
    send_socket = None
    youtube_command = None
    video_dir = None
    youtube_url = "youtube.com"

    # Initializer / Instance Attributes
    def __init__(self, receive_address, send_address, video_dir):
        Thread.__init__(self)
        self.receive_socket = SocketReceiver(receive_address)
        self.send_socket = SocketSender(send_address)
        self.video_dir = video_dir
        self.youtube_command = "youtube-dl --ignore-errors -f 140 -o '" + self.video_dir + "/%(id)s' --restrict-filenames "

    def run(self):
        while True:
            try:
                search_string = self.receive_socket.getMessage()
                if (self.youtube_url in search_string):
                    # Its either a direct link to a playlist or a video
                    if (len(search_string) == 12):
                        # Regular video urls are 12 characters
                        call(self.youtube_command + " --max-filesize 100m --max-downloads 1 " + search_string,
                             shell=True)

                    elif (len(search_string) == 35):
                        # Playlist urls are 35 characters\
                        call(self.youtube_command + ' --max-downloads 25 ' + search_string, shell=True)
                    else:
                        # Something bad happened
                        print("Unable to identify valid url from value:" + search_string)
                else:
                    # We need to search by keyword and find a relevant video
                    call(
                        self.youtube_command + ' --max-filesize 100m --max-downloads 1 --default-search \"ytsearch\" \"' + search_string + '\" ',
                        shell=True)
            except KeyboardInterrupt:
                raise KeyboardInterrupt

    def stop(self):
        pass
