"""Accessing Strings


You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4
There are 4 vowels in the given text."""


#your code goes here
i=input()
count=0
for s in i:
    if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
        count+=1
print(count)
