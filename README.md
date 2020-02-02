# Udacity_DataStructure-Algorithms_project 0
My Projects and codes during the Udacity Nanodegree Program


# Complexity Analysis:

# Task 0

Since the data is visible sorted, the data can be directly took from the top / bottom of the files ( lists )
So the complexity of time and Space would be O(1)

# Task 1

This task was necessary to sweep all the lists / files and add to a set, remaining that way, just the unique values. This analysis need to put into account the length of both each list, meaning O(n+m). Complexity O(n)

# Task 2

Task 2 had to run loop over loop, which means it is dependent of 2 variables, the number of lines on calls + the number of unique values that are the prime key. So O(n*n) = Complexity O(n²)

# Task 3

That task was necessary to do find and read the lines of each file. That consuming O(n) but since the result had to be printed sorted it implies in a O(m log m) algorithm usage(n + (m log m) ) . Complexity O(n long n)

# Task 4

In order to separate the uniques it was necessary to iterate over all line O(n) than it was necessary to check if the values didn`t show up into the called + text number O(n) and the result had to be printed in a sorted manner. O(n+n+n log n). Complexity O(n log n)
