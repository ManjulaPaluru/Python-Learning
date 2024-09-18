# find out pair from given sum from array

def twosum(arr,sum):
    print(arr) # [5, 7, 4, 3, 9, 8, 29, 21]
    print(sorted(arr)) #[3, 4, 5, 7, 8, 9, 21, 29]
    left = 0
    right = len(arr)-1
    while(left <= right):
        if(arr[left]+arr[right] > sum):
            right = right-1
        elif(arr[left]+arr[right] < sum):
            left = left+1
        elif(arr[left]+arr[right] == sum):
            print("pair from given sum is: " ,arr[left],"&", arr[right])
            right =right-1
            left = left+1

arr = [5, 7, 4, 3, 9, 8, 29, 21]
sum = 30
twosum(arr,sum)
