from time import sleep
from subprocess import call


try:
	while True:
		with open("playlistqueue.txt", "r") as myfile:
			url = myfile.readline()

		if not url :
			sleep(10)
		else:
			call("omxplayer" + " -o local" + " " + url , shell=True)	
			with open('playlistqueue.txt', 'r') as fin:
				data = fin.read().splitlines(True)
			with open('playlistqueue.txt', 'w') as fout:
				fout.writelines(data[1:])
	#finding if this song should be played again
			my_file = "playlistqueue.txt"
			my_string = url
			infile = open(my_file,"r")
			numlines = 0
			found = 0
			for line in infile:
				numlines += 1
				found += line.count(my_string)
			infile.close()
	################################################
			if found == 0:
				call("rm" + " " + url , shell=True)
			sleep(1)
except KeyboardInterrupt:
	pass
