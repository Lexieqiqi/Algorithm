# Merge sort

# Divide and conquer

def mergeSort(unsorted,low,high):
	if low < high:
		mergeSort(unsorted,low,(low+high)//2)
		mergeSort(unsorted,(low+high)//2+1,high)
		merge(unsorted,low,high)
	return unsorted

def merge(unsorted,low,high):
	list1 = unsorted[low:(low+high)//2+1]
	list2 = unsorted[(low+high)//2+1:high+1]
	list1.append(float("inf"))
	list2.append(float("inf"))
	i = 0
	j = 0
	k = low
	for k in range(low,high+1):
		if list1[i] <= list2[j]:
			unsorted[k] = list1[i]
			i = i + 1
		else:
			unsorted[k] = list2[j]
			j = j + 1
	return unsorted

l = []
f = open("./IntegerArray.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break

#print(l)
test_list = [2,3,1,6,3,9,0,8]
mergeSort(l,0,len(l)-1)
print(l)