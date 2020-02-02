#!/usr/bin/env python
# coding: utf-8

# In[35]:


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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
all_callers = set()
for number in calls:
    all_callers.add(number[0])

not_contain = set()

for each1 in calls:
    not_contain.add(each1[1])
    
for each2 in texts:
    not_contain.add(each2[0])
    not_contain.add(each2[1])

result = set()    
for each in all_callers:
    if each not in not_contain:
        result.add(each)
        
print("These numbers could be telemarketers:")
for i in sorted(result):
    print(i)
