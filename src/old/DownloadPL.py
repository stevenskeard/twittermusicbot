from subprocess import call

with open('downloadqueue.txt', 'r') as mydl:
    url = mydl.readline()

url = url[:-1]

if len(url) == 34:
    call('youtube-dl --get-filename --ignore-errors --max-downloads 25 -o "%(id)s"' + ' ' + url + ' | tee logfile.txt',
         shell=True)

else:
    call(
        'youtube-dl --get-filename --max-downloads 1 --ignore-errors -o "%(id)s"' + '  --default-search \"ytsearch\" \"' + url + '\" ' + ' | tee logfile.txt',
        shell=True)

# call('youtube-dl --get-filename --ignore-errors -o "%(id)s"' + ' ' + url + ' 2>&1 | tee logfile.txt', shell=True)

# with open('logfile.txt', 'r') as myfile:
#	data = myfile.read().splitlines(True)
# with open('playlistqueue.txt', 'a') as mypl:
#	mypl.writelines(data)

# call('rm logfile.txt', shell=True)
