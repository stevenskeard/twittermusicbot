#!/usr/bin/env python

import os
import errno
from AudioPlayer import AudioPlayer
from SearchAndDownload import SearchAndDownload
from Twitter import Twitter

#Define the paths to be used
rootDir = '/tmp/twittermusicbot'
downloadDir = rootDir + '/downloads'
socketDir = rootDir + '/sockets'
downloadAddress = '/tmp/twittermusicbot/socket/downloadqueue'
playAddress = '/tmp/twittermusicbot/socket/playqueue'

twitterThread = None
searchAndDownloadThread = None
audioPlayerThread = None

#Make sure we are main
if __name__ == '__main__':

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

#Shouldn't ever reach here but include an exit for safety's sake
raise SystemExit