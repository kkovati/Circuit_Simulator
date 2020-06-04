import time
from simulator.misc import LoadingBar


print('1.line')

lb = LoadingBar(1000, 'Test')
for i in range(1000):
    time.sleep(0.001)
    lb()
    
print('2.line')