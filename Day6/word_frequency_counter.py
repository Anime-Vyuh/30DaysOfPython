import string

def remove_punction(para):
    new = ""
    for i in para:
        if i in string.punctuation:
            pass
        else:
            new+=i
    return new

sample_input = input("Enter a sentence:")
word_dictionary = dict() # or {}
sentence = remove_punction(sample_input)

for word in sentence.split():
    word_dictionary[word] = 1 if word not in word_dictionary else word_dictionary[word]+1

print(word_dictionary)