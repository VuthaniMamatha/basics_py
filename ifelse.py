"""Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer,n .

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird"""




i=int(input())
if i%2==0 and (i in range(2,5)):
    print("Not Weird")
elif i%2==1:
    print("Weird")
elif i%2==0 and (i in range(6,21)):
    print("Weird")
elif i>20 and i%2==0:
    print("Not Weird")
