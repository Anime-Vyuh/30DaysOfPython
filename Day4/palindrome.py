"""Program 1: Palindrome
Malayalam, madam, civic. Now why am I mentioning this words. Palindrome are
those words which are pronounced the same even if you read them in reverse
way. The word is Palindrome if it is equal to the reverse of the word.
Sample Input: madam
the reverse of the word is also madam
Thus it is a Palindrome
Sample Input: professor
the reverse of the word is also rosseforp
Thus it is not a Palindrome
"""
palindrome = input("Enter a word: ")
reverse = palindrome[::-1]
if reverse == palindrome:
    print("Yes it is a Palindrome")
else:
    print("No it is not a Palindrome")
