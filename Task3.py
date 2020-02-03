#!/usr/bin/env python
# coding: utf-8

# In[77]:


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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
called_numbers = []
receivers_bangalore = 0

for eachlinecalls in calls:
    if eachlinecalls[0].find('080') > 0:
        called_numbers.append(eachlinecalls[1])
        if eachlinecalls[0].find('080') > 0 and eachlinecalls[1].find('080') > 0:
            receivers_bangalore += 1
            
total_calls_bangalore = len(called_numbers)
        
area_codes = set()        
for line in called_numbers:
    if line.find(')') == 4:
        area_codes.add(line[0:5])
    if line.find(')') == 5:
        area_codes.add(line[0:6])
    if line.find(')') == 6:
        area_codes.add(line[0:7])
    if line[0] == "7" or line[0] == "8" or line[0] == "9":
        area_codes.add(line[0:4])
    if line[0:2] == "140":
        area_codes.add(line[0:3])
        

        
""" Task 3 A - The unique area codes that received calls were: """        
print('The numbers called by people in Bangalore have codes:')

for i in sorted(area_codes):
    print(i)    

""" Task 3 B  Percetage of Calls loclaly in Bagalore: """  

percentage = round(receivers_bangalore/total_calls_bangalore * 100,2)
print(str(percentage) + ' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
