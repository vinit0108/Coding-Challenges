import os
from datetime import datetime


def outage_interval(trade_data) -> str:
    # sorting the trade data
    trade_data.sort()
    
    # setting the prev DateTime object to be null
    prev = None
    
    # looping through the list
    for index in range(len(trade_data)):
        i = trade_data[index]
        
        # splitting the object to make the seconds part
        # a whole number
        i = i.split(':')
        i[2] = str(int(float(i[2])))
        time = i[0] + ':' + i[1] + ':' + i[2]
        
        # datetime object for the time
        current = datetime.strptime(time, '%H:%M:%S').time()
        
        # checking if the difference between the previous and current time is more
        # than 60 seconds
        if index > 0 and current.second - prev.second > 1:
            return trade_data[index - 1] + '-' + trade_data[index]
        
        # setting the current time as previous
        prev = current


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    trade_data_count = int(input().strip())

    trade_data = []

    for _ in range(trade_data_count):
        trade_data_item = input()
        trade_data.append(trade_data_item)

    result = outage_interval(trade_data)

    fptr.write(result + '\n')

    fptr.close()

