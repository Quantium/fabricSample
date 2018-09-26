from fabric import SerialGroup as Group
results = Group('pi@192.168.8.103','pi@192.168.8.104','pi@192.168.8.105','pi@192.168.8.107').run('hostname')
print(results)
