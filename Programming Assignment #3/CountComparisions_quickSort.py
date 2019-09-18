import random

def findMiddle(arr,x,y,z):
	tri = [arr[i] for i in [x,y,z]]
	tri.sort()
	return tri[1]


def swap(arr,x,y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr

def quickSort(arr,low,high):
	if low < high:
		arr,mid = Partition(arr,low,high)
		arr,count1 = quickSort(arr,low,mid-1)
		arr,count2 = quickSort(arr,mid+1,high)
		return arr,high-low+count1+count2
	else:
		return arr,0

# using the first element as a pivot
def Partition(arr,low,high):
	p = arr[low]
	i = low+1
	j = i
	while j <= high:
		if arr[j]<=p:
			swap(arr,i,j)
			i = i+1
		j = j+1
	swap(arr,low,i-1)
	return arr,i-1


# using the final element as a pivot 164123
# def Partition(arr,low,high):
# 	p = arr[high]
# 	swap(arr,low,high)
# 	i = low
# 	i = low+1
# 	j = i
# 	while j <= high:
# 		if arr[j]<=p:
# 			swap(arr,i,j)
# 			i = i+1
# 		j = j+1
# 	swap(arr,low,i-1)
# 	return arr,i-1

# using the median-of-three pivot role 138382
# def Partition(arr,low,high):
# 	p = findMiddle(arr,low,high,(high+low)//2)
# 	swap(arr,low,arr.index(p))
# 	i = low
# 	j = i
# 	while j <= high:
# 		if arr[j]<=p:
# 			swap(arr,i,j)
# 			i = i+1
# 		j = j+1
# 	swap(arr,low,i-1)
# 	return arr,i-1

#l = [3,8,2,5,1,4,7,6]

l = []
f = open("../sort/QuickSort.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break

print(quickSort(l,0,len(l)-1))
