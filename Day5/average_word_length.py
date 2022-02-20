"""
Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number.

Input Format:
A string containing multiple words. Input: What a drag Shikamaru

Output Format:
A number representing the average length of each word, rounded up to the nearest whole number.  Output: 5

Explanation:
The string in question has 4 words with a total of 18 letters (spaces do not count). The average word length is 4.50 letters, rounding it up to the nearest whole numbers results in 5.
"""
import math
import string
data = input().split(' ')
avg_word = []
for calc in data:
    for check in calc:
        if check in string.punctuation:
            pass
        else:
            avg_word.append(check)

print(math.ceil(len(avg_word)/len(data)))
