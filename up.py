from fabric import SerialGroup as Group
# Put the raspberries IP addresses here
# The pi user should be replaced
results = Group('pi@192.168.8.102','pi@192.168.8.104','pi@192.168.8.107').run('sudo apt-get upgrade')
print(results)
