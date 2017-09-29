from subprocess import call

with open('playlistqueue.txt', 'r') as myfile:
	data = myfile.read().splitlines(True)
	
for i in range(len(data)) :
	call('rm ' + data[i], shell=True)

with open('playlistqueue.txt', 'w') as myfile:
	numLines = len(data)
	del data[:numLines]
	myfile.writelines(data)


