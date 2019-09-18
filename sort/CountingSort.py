# Counting sort
# in this algorithm, we dont compare elements while sorting
# It is a sorting algorithm in which we sort a collection of elements


# Find the minimum and maximum of the input
# count the currency of numbers appering in the input
# Adding each number index to indicate their index. sumCount
# Scan the input array and then by the index we can put the value into the sumCount point

def CountingSort(arr):
	max_ = max(arr)
	min_ = min(arr)
	index = [i for i in range(min_,max_+1)]
	sumCount = {}.fromkeys(index,0)

	for i in arr:
		sumCount[i] = sumCount[i] + 1
			
	for j in index[1:]:
		sumCount[j] = sumCount[j] + sumCount[j-1]
	sortedarr = [0]*len(arr)

	index = len(arr)-1
	while index >= 0:
		sortedarr[sumCount[arr[index]]-1] = arr[index]
		sumCount[arr[index]] = sumCount[arr[index]] - 1
		index = index-1
	return sortedarr

# l = [2,45,111,32,45,3,5,6,2,89,3]

l = []
f = open("./IntegerArray.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break

print(CountingSort(l))
