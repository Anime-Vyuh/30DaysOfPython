"""
Caesar Cipher
Caesar cipher uses keys, which encrypt the message differently
depending on which key is used. The keys for the Caesar cipher are the
integers from 1 to 26(a-z). Based On the key from 1-26, the given message is encoded ahead with the given key.

Sample Input:
Security key: 3
Message: anime

Sample Output:
dqlph

Explaination: key=3, first character of message=a a+3=d(b,c,d),
in the same way, n+3 = q (o,p,q)
i+3 = l (j,k,l)
m+3 = p (n,o,p)
e+3 = h (f,g,h)
"""
import string

with open("actual_message.txt","w") as file:
    message = input("Enter the Best Anime you have watched:")
    file.write(message)
file.close()

def security_key():
    while True:
        key = int(input("Security Key(1-26):"))
        if key not in range(1,27):
            continue
        return key

key = security_key()
encrypt = open("actual_message.txt","r").read()
upper_c = string.ascii_uppercase
lower_c = string.ascii_lowercase

encode = ''
for i in encrypt:
    if i in upper_c:
        encode+=upper_c[upper_c.index(i)+key-26] if upper_c.index(i)+key>25 else upper_c[upper_c.index(i)+key]
    elif i in lower_c:
        encode+=lower_c[lower_c.index(i)+key-26] if lower_c.index(i)+key>25 else lower_c[lower_c.index(i)+key]
    else:
        encode+=' '

with open("encrypted.txt","w") as new_file:
    new_file.write(encode)
new_file.close()
print("Success, Message Encrypted")
