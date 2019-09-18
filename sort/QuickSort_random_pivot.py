import random

def swap(arr,x,y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr

def quickSort(arr,low,high):
	if low < high:
		pivot = random.randint(low,high)
		arr,mid = Partition(arr,pivot,low,high)
		quickSort(arr,low,mid-1)
		quickSort(arr,mid+1,high)
		return arr

def Partition(arr,pivot,low,high):
	p = arr[pivot]
	swap(arr,low,pivot)
	i = low+1
	j = i
	while j <= high:
		if arr[j]<=p:
			swap(arr,i,j)
			i = i+1
		j = j+1
	swap(arr,low,i-1)
	return arr,i-1

#l = [3,8,2,5,1,4,7,6]

l = []
f = open("./QuickSort.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break

print(quickSort(l,0,len(l)-1))
