import requests
from time import sleep
from ttp import ttp
from twython import TwythonStreamer

# Search terms
TERMS = '#musicatsteves'

# Twitter application authentication
APP_KEY = '0bVzq7nfOYBd061IbgHwjYWyy'
APP_SECRET = 'krxt7tmb1qZtZF8H1yEEnwvjlqgjgIfR0B3pDwILXBinpWYx5o'
OAUTH_TOKEN = '2961482583-dplTTmQpwk72JO2FAqeKiKlMtw0DRDqDJgXEXqd'
OAUTH_TOKEN_SECRET = 'idE222rHbVSAwbdq9OY5Qj6rbhQomhXnpaaqBfhes2wvV'


# Setup callbacks from Twython Streamer
class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        # sleep(10)
        print "Song inc."
        print '\n'
        if 'text' in data:
            tweet = data['text'].encode('utf-8')
        # data['text'] is of type: string
        with open("downloadqueue.txt", "a") as myfile:

            parser = ttp.Parser()
            result = parser.parse(tweet)
            rawhtml = str(result.html)
            search = rawhtml.split("search:")
            # print(search)
            # print(type(search))
            # print(len(search))
            if result.urls:
                tco = result.urls[0]
                link = requests.get(tco)
                ytlink = str(link.url)
                ytsplit = ytlink.split("v=")
                ytsplit2 = ytlink.split("list=")
                if len(ytsplit) > 1:
                    ytid = ytsplit[1]
                    ytvid = ytid[:11]
                    myfile.write(ytvid.encode('utf-8'))
                    myfile.write("\n".encode('utf-8'))
                if len(ytsplit2) > 1:
                    ytid2 = ytsplit2[1]
                    ytpid = ytid2[:34]
                    myfile.write(ytpid.encode('utf-8'))
                    myfile.write("\n".encode('utf-8'))
            if len(search) > 1:
                # write search command to downloadqueue
                # print("inif")
                # searchstring = "https://www.youtube.com/results?search_query="
                # myfile.write(searchstring.encode('utf-8'))
                myfile.write(search[1].encode('utf-8'))
                myfile.write("\n".encode('utf-8'))

    def on_error(self, status_code, data):
        print status_code
        sleep(14)
    # Want to stop trying to get data because of the error?
    # Uncomment the next line!


# self.disconnect()

# Create streamer

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=TERMS)
