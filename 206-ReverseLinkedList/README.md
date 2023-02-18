# Complexity Ananlysis

## Solution 1

Time Complexity : O( n ) where n is the number of elements in the linked list
Space Complexity : O( n ) where n is the number of elemnts in the linked list

## Solution 2

Time Complexity : O( n ) where n is the number of elements in the given linked list
Space Complexity : O( 1 ) 

## Solution 3

Time Complexity : O( n ) where n is the number of elements in the given linked list
Space Complexity : O( 1 ) 


# Notes 

## Solution 1

In this solution firstly the linked list is read and the values is stored in a regular list. Then another linked list is created with the values from the list in a reverse order.

## Solution 2 

This solution uses a 2-pointer approach. In this solution we define 2 pointers which are the current node and the previous node. The previous node is assigned to the null value initially. A while loop is executed which firstly stores the node which is next to the the cuurrent node and then proceeds to point the currents node to the previous one and then moves to the next nodes by changing the current to the next and prevoius to the current.

## Solution 3

This solution uses a 3-pointer approach, In this solution we define 3 pointer which are the current, the previous and the the next node. The prevoius node is assigned to the null value initially. A while loop is executed which points the current to the previous node and then moves to the next node by changing the currents to next, the prevoius to current and next to the next node of the current. As a result this loop is only able to run till the second last node, and hence once the loop has ended we need to execute the operation of pointing the current node to the prevoius node one more time.
