"""
Program 1: Piglatin

Input Format
A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization), e.g., "nevermind you’ve got them"

Output Format
A string of the same sentence in Pig Latin.
e.g., output: "evermindnay ouveyay otgay hemtay"

Explanation
The output should be the original sentence with each word changed so that they first letter is at the end and then -ay is added after that.
"""

word=input().lower().split()
new=[]
for i in word:
    k=i[1:]+i[0]+'ay'
    new.append(k)
print(' '.join(new))

#or
"""
import string
l=input('Enter a text:').lower().split()
new=[]
punc=string.punctuation
for i in l:
    for j in i:
        if j in punc:
            del j
        else:
            new.append(j)
    k=''.join(new)
    new.append(' ')

print(len(''.join(k.rstrip())))
"""