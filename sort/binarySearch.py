# Binary Search

def binarySearch(x,middle,arr):
	if x < arr[middle-1]:
		binarySearch(x,middle//2,arr)
	elif x == arr[middle-1]:
		return middle
	else:
		binarySearch(x,(len(arr)+middle+1)//2,arr)

arr = [1,2,3,4,5,6,7,8,9,10]

print(binarySearch(1,5,arr))