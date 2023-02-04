# Complexity Ananlysis

## Solution 1

O( 

# Notes 

## Solution 1

Firstly we need to understand that if the number lies in the range of 2-5, it will never be a happy number. So firstly the program checks if the number the number is 1, if so then it simply returns True. If not then it further checks if it lies in the range of 2-5, and if that is the case then it returns False, because of the above mentioned reason. If none of these initial conditions is satisfied then it starts performing the given operations to obtain the the sum of the squares of each digit of the number. Then this sum is checked with the same conditions, and if none of them are satisfied then the loop continues until they are satisfied.
