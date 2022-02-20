def search(nums,target):
    nums.sort()
    beg,end=0,len(nums)-1
    while beg<=end:
        mid = (beg+end)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            beg=mid+1
        else:
            end=mid-1
    return -1

target = int(input("Enter a target element"))
print(search([1,22,4,56,446,56,2,5],target))