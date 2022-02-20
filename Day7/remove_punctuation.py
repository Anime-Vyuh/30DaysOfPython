"""
Remove Punctuation From a Sentence
Read a File with Text inside it and remove punctuations from the text.

Sample Input: T%hi/s senten$ce, th@is diffi&^cu)()lt t*o re!a+d|
Sample Output: This sentence this difficult to read

[Note: Save the Sample Input in some file]
"""
import string

punc = string.punctuation
with open("reference.txt") as ref_file:
    content = ref_file.read()
ref_file.close()

print("Before: {}".format(content))

proper_text = ""
for word in content:
    if word in punc:
        pass
    else:
        proper_text+=word

print("After: {}".format(proper_text))
