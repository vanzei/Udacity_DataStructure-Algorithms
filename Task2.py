"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone = set()

for eachlinecalls in calls:
    phone.add(eachlinecalls[0])
    phone.add(eachlinecalls[1])
    
Dict = {}

for unique in phone:
    Dict[unique] = 0
    for each in calls:
        if unique == each[0] or unique == each[1]:
            Dict[unique] = int(Dict[unique]) + int(each[3])

longest = max(Dict.items(), key=operator.itemgetter(1))[0]
print(longest + " spent the longest time, " + str(Dict[longest]) +" seconds, on the phone during September 2016.")