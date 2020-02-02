"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique = set()

for eachlinetext in texts:
    unique.add(eachlinetext[0])
    unique.add(eachlinetext[1])

for eachlinecalls in calls:
    unique.add(eachlinecalls[0])
    unique.add(eachlinecalls[1])



count= len(unique)
    
print("There are " + str(count) + " different telephone numbers in the records")
