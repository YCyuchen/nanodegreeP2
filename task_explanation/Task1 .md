# Task1 
Square Root of Integer
## Problem description
Find the square root of the integer without using any Python library.
The expected time complexity is O(log(n))

## Solution
Considering time complexity O(log(n)), and we need to find the square root of the integer, [Binary search ](https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/bd252a0b-e9e7-473b-bcc1-bc7e3153568b/lessons/04407d33-d27a-4732-9e4a-df6fe788a569/concepts/9b80af2c-fbbe-458a-9c31-eec3a53c9346) for the sorted array should be consider. 
*How to search the square root through binary search?*
Well, first we initialize the left = 0 and right=inputer_num. Then we always judge the square of the center number with with the input. 
$center^2 <= number < (center + 1) ^ 2$
And we adjust the left and right value according to the up formula.

Time complexity **Big O equals to** $O(logn)$.  n is the value of the input element.
Space complexity **Big O equals to** $O(3)=O(1)$ Since we only need to record 3 elements' value: left, right, center**