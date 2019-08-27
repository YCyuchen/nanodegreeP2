# Task6 
# Problem description 
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

# Solution
First initialize the min and max as the first element of the input_list. Then just traverse the list index one by one and compare each list item's value with the min and max, the revalue the min and max.

Time complexity is $O(N)$, N is the number of element in list
Space complexity is $O(2)->O(1)$, 2 means those two param store the min and max value.