#!/usr/bin/env python

from .AudioPlayer import AudioPlayer
from .SearchAndDownload import SearchAndDownload
from .Twitter import Twitter

#Define the paths to be used
rootDir = '/tmp/twittermusicbot'
downloadDir = rootDir + '/downloads'
socketDir = rootDir + '/sockets'
downloadAddress = '/tmp/twittermusicbot/socket/downloadqueue'
playAddress = '/tmp/twittermusicbot/socket/playqueue'

#Make sure we are main
if __name__ == '__main__':

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
        twitterThread = Twitter("Twitter", downloadAddress)
        searchAndDownloadThread = SearchAndDownload("SearchAndDownload", downloadAddress, playAddress)
        audioPlayerThread = AudioPlayer("AudioPlayer", playAddress)

        #Start all the threads
        twitterThread.start()
        searchAndDownloadThread.start()
        audioPlayerThread.start()

        while True:
            try:

            except:

    finally:
        twitterThread.stop()
        searchAndDownloadThread.stop()
        audioPlayerThread.stop()

raise SystemExit
