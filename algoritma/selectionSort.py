import time
from colors import *

def selection_sort(data, drawData, timeTick):
    for i in range(0, len(data)-1):
        minj = i
        minx = data[i]
        for j in range(i + 1, len(data)):
            if data[j] < minx :
                minj = j
                minx = data[j]

        data[minj] = data[i]
        data[i] = minx
        drawData(data, [RED if j == minj or j == i else DARK_BLUE for j in range(len(data))] )
        time.sleep(timeTick)

    drawData(data, [DARK_BLUE for j in range(len(data))])
    