"""String Operations


Let's test your coding skills!
Take a string as input and output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string.

Sample Input:
data

Sample Output:
d
aa
ttt
aaaa
Hint: Use a loop to iterate over the string, keeping the position number of the current iteration in a variable. Then use multiplication to repeat the letters."""

#your code goes here
s=input()
index=1
for i in s:
    print(i*index)
    index+=1
