def swap(arr,x,y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr

def quickSort(arr,low,high):
	if low<high:
		#print("The arr before sort:",arr[low:high+1])
		pivot = arr[low]
		i = low+1
		j = low+1
		while j <= high:
			if arr[j]<=pivot:
				if i!=j:
					swap(arr,i,j)
				i = i+1
			j = j+1
		#print("The pivot is :",pivot)
		swap(arr,low,i-1)
		#print(arr[low:high+1])
		quickSort(arr,low,i-2)
		quickSort(arr,i,high)
		return arr

#l = [3,8,2,5,1,4,7,6]

l = []
f = open("./IntegerArray.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break

quickSort(l,0,len(l)-1)

print(l)