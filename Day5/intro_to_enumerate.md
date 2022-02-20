## Introduction to Enumerate

Before knowing Enumerate lets look into an example as usual. Consider a List and print the elements of the list with their index number.
```py
>>> myanimelist = ["One Piece","Gintama","Attack On Titan","Code Geass","Monster"]

>>> for i in range(len(myanimelist)):
...  print(i+1,myanimelist[i])
...
1 One Piece
2 Gintama
3 Attack On Titan
4 Code Geass
5 Monster
```

The same code lets code it with enumerate.

```py
>>> for index,anime in enumerate(myanimelist,1):
...  print("{}:{}".format(index,anime))
...
1:One Piece
2:Gintama
3:Attack On Titan
4:Code Geass
5:Monster

>>> for index,anime in enumerate(myanimelist):
...  print("{}:{}".format(index,anime))
…

0:One Piece
1:Gintama
2:Attack On Titan
3:Code Geass
4:Monster
```

``Enumerate`` makes our job easy by taking both index and values in one go. Understanding enumerate is easy. We have taken two examples in enumerate function. Enumerate takes two parameters, the first parameter is the iterable sequence such as lists, string, range. And the second parameter is the start index includes a integer value.