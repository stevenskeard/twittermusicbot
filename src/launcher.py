from subprocess import call

call("sudo python TwitterMonitor.py" + " &", shell = True)
call("sudo python DownloadYT.py" + " &", shell = True)
call("sudo python PlayMusic.py" , shell = True)


