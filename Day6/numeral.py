"""
Input Format:
A string of the phrase in its original form (lowercase).

Output Format:
A string of the updated phrase that has changed the numerals to words.
Sample Input: I need 2 pumpkins and 3 apples

Sample Output: I need two pumpkins and three apples
"""

def numeral(num,n):
    nonum=dict()
    for i in n:
        nonum[str(i)]=num[i-1]
    return(nonum)

num=['one','two','three','four','five','six','seven','eight','nine','ten']
n=range(1,11)
nonumeral=numeral(num,n)
data=input('').split()
new_data=[]
for word in data:
    if word in nonumeral.keys():
        word=nonumeral[word]
    new_data.append(word)
print(' '.join(new_data))
