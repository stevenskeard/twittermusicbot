#!/usr/bin/env python

import os
import errno
from AudioPlayer import AudioPlayer
from SearchAndDownload import SearchAndDownload
from Twitter import Twitter

class Controller:

    def initialize(self):

        #Print something so its easier to check that it is running
        print("TwitterMusicBot -- Initializing")

        #Define the paths to be used
        rootDir = '/tmp/twittermusicbot'
        downloadDir = rootDir + '/downloads'
        socketDir = rootDir + '/sockets'
        downloadAddress = '/tmp/twittermusicbot/socket/downloadqueue'
        playAddress = '/tmp/twittermusicbot/socket/playqueue'

        #Define the thread references for use below
        twitterThread = None
        searchAndDownloadThread = None
        audioPlayerThread = None

        # Initialization is done so print to know that we're just looping from here on out
        print("TwitterMusicBot -- Running")

        #Wrap the whole thing in a try to ensure the threads get exited in the finally clause
        try:

            #Make sure the directories exists
            try:
                os.makedirs(downloadDir)
                os.makedirs(socketDir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            #Make sure our sockets aren't already in use
            try:
                os.remove(downloadAddress)
                os.remove(playAddress)
            except OSError:
                pass

            #Create all the threads we will need
            twitterThread = Twitter(downloadAddress)
            searchAndDownloadThread = SearchAndDownload(downloadAddress, playAddress)
            audioPlayerThread = AudioPlayer(playAddress)

            #Assign daemon true so they exit when parent does
            twitterThread.daemon = True
            searchAndDownloadThread.daemon = True
            audioPlayerThread.daemon = True

            #Start all the threads
            twitterThread.start()
            searchAndDownloadThread.start()
            audioPlayerThread.start()

            #Just loop forever, or until we get an exception at least
            while True:
                try:
                    pass
                except:
                    raise Exception("Exiting")

        finally:
            if twitterThread:
                twitterThread.stop()
            if searchAndDownloadThread:
                searchAndDownloadThread.stop()
            if audioPlayerThread:
                audioPlayerThread.stop()


#Make sure we are main
if __name__ == '__main__':
    controller = Controller()
    controller.initialize()

#Shouldn't ever reach here but include an exit for safety's sake
raise SystemExit