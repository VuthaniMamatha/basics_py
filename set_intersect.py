"""Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.
You can use the split() function to get a list of words in a string and then use the set() function to convert it into a set. For example, to convert the list x to a set you can use: set(x)"""

s1 = input()
s2 = input()
l1=s1.split()
l2=s2.split()
s=set(l1)&set(l2)
print(len(s))
