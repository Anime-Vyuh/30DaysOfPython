def bubble_sort(container):
    for i in range(len(container)):
        for j in range(i+1,len(container)):
            if container[i]>container[j]:
                container[i],container[j]=container[j],container[i]

    return container

print(bubble_sort([5,1,4,2,8]))