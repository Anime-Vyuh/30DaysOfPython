def dejavu(text):
    count=0
    new=list()
    for i in text:
        if i not in new:
            new.append(i)
        else:
            count=1
            return count

word=list(input())
count=dejavu(word)
if count==1:
    print('Deja Vu')
else:
    print('Unique')