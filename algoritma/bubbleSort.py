import time
from colors import *

def bubble_sort(data, drawData, timeTick):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1] :
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                drawData(data, [YELLOW if i == j or i == j+1 else RED for i in range(len(data))] )
                time.sleep(timeTick)
        drawData(data, [RED for i in range(len(data))])
  