import subprocess
import json

p = subprocess.Popen(['docker', 'ps'], stdout=subprocess.PIPE)

lineNumber = 1
for line in p.stdout.readlines():
    fields = line.split()
    if lineNumber > 1:
        containerId = fields[0]
        containerName = fields[-1]
        
        inspect = subprocess.run(['docker', 'inspect', containerId], stdout=subprocess.PIPE)
        data = json.loads(inspect.stdout.decode('utf-8'))
        networkMode = data[0]['HostConfig']['NetworkMode']
        print (containerName.decode('utf-8'), data[0]['NetworkSettings']['Networks'][networkMode]['IPAddress'])
    lineNumber += 1

