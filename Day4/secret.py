"""
Program 4: Secret Message
A string of your message in its normal form. Ask user for a input and convert that
message into a secret message. The way you should do this is, say the message is
converted based on backwards alphabets i.e., a is replaced with z, a=z, b=y, c=x,
d=w, e=v, f=u, g=t and so on..
Output Format:
A string of your message once you have encoded it (all lower case).
Sample Input: Pirate King
Sample Output: krizgv prmt
Explanation:
If you replace each letter in 'Pirate King' with the corresponding letter in a
backwards version of the alphabet, you get 'krizgv prmt'.
"""

import string
user_data = input().lower()
backwards = string.ascii_lowercase[::-1]
back_alpha = ''
for alpha in user_data:
    if alpha == ' ':
        back_alpha+=' '
    else:
        index = string.ascii_lowercase.index(alpha)
        back_alpha+=backwards[index]
print(back_alpha)