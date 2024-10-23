from mgq import MgqClient
import datetime

client = MgqClient("tcp://broker:5555")

startTime = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
timeNow = datetime.datetime.now()
print('Starting at - '+ startTime)
lastCount = ''
for i in range(50000):
    response = client.send_message("work", "hello"+str(i+1))
    lastCount = response.split(' ')[0].replace('hello', '')
timeAfter = datetime.datetime.now()
elapsed = timeAfter - timeNow
endTime = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print('Ended at - '+ endTime)
print('Last count - '+ lastCount)
print('Total time taken in (ms) - '+ str(int(elapsed.total_seconds() * 1000)))