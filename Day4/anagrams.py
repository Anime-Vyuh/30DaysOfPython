"""
Program 2: Anagrams
Input : s1 = "luffy"
        s2 = "fufly"
Output : Pair of words are anagrams

Sample Input : s1 = "luffy"
        s2 = "naruto"
Sample Output : Not a anagrams

Sample Input : s1 = "bad"
        s2 = "dad"
Sample Output : Not a anagrams

Sample Input : s1 = "cool"
        s2 = "loco"
Sample Output : Pair of words are anagrams
"""
word1=input("Enter first string:").lower()
word2=input("Enter second string:").lower()
if(sorted(word1)==sorted(word2)):
    print('Pair of words are anagrams')
else:
    print('Not a anagrams')