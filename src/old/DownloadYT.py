#call youtube-dl with batch file argument

from subprocess import call
import os.path
from time import sleep
import sys


DIR = "/TwitterMusicBot/"
youtubecmd = "youtube-dl --ignore-errors -f 140 -o '%(id)s' --restrict-filenames "
#call("youtube-dl" + " --ignore-errors -f 140 "  + data[i] + ' -o "%(id)s" --restrict-filenames --max-downloads 1', shell=True)



try:
	while True:
			with open ('downloadqueue.txt', 'r') as myfile:
				firstline = myfile.readline()

			if not firstline :
				sleep(1)
			else:	
				with open ('downloadqueue.txt', 'r') as myfile:
					data = myfile.read().splitlines(True)
					numLines = len(data)

				for i in range(len(data)): ############Individual Songs

					if (len(data[i]) == 12) :

						with open('playlistqueue.txt', 'a') as mypl:
							mypl.writelines(data[i])
						call(youtubecmd + " --max-filesize 100m --max-downloads 1 " + data[i], shell=True)
						
					elif (len(data[i]) == 35) :############ Playlists

						call(youtubecmd + ' --max-downloads 25 ' + data[i], shell=True)
						print("Starting name download")
						call("sudo python DownloadPL.py", shell=True)
						print("Finished name download")
						with open('logfile.txt', 'r') as mylog:
							datalog = mylog.read().splitlines(True)
						with open('playlistqueue.txt', 'a') as mypl:
							mypl.writelines(datalog)

					else:################Search Queries

						call(youtubecmd + ' --max-filesize 100m --max-downloads 1 --default-search \"ytsearch\" \"' + data[i] + '\" ' , shell=True)
						print("Starting name download")
						call("sudo python DownloadPL.py", shell=True)
						print("Finished name download")
						with open('logfile.txt', 'r') as mylog:
							datalog = mylog.read().splitlines(True)
						with open('playlistqueue.txt', 'a') as mypl:
							mypl.writelines(datalog)
						

					del data[i]
				
				with open('downloadqueue.txt', 'w') as myfile:	
					myfile.writelines(data)
				print("Fin. Round")

except KeyboardInterrupt:	
	pass	
	
