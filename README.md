TwitterMusicBot (2019) is a rewrite of the original that I wrote around 2013

TwitterMusicBot is a simple Python bot that monitors twitter for a hashtag.
It parses tweets containing the hashtag and search to find a match on YouTube.
It will download the best match (top result from the search parameters) as long as it is less than 100MB (Avoiding things like 10 hour mixes...)
Then it will add them to a queue of songs to play

References:
https://hub.docker.com/_/python/?tab=description
https://stackoverflow.com/questions/9361625/how-to-make-a-socket-server-listen-on-local-file
https://realpython.com/python3-object-oriented-programming/
https://docs.python.org/2/library/socket.html
https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
https://stackoverflow.com/questions/15365406/run-class-methods-in-threads-python
https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used