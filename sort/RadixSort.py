# Radix Sort

def RadixSort(arr):
	max_ = max(arr)
	d = 0
	while max_>0:
		max_ = max_//10
		d = d + 1
	section_arr = [0]*len(arr)
	for i in range(d):
		for j in range(len(arr)):
			if arr[j]//(pow(10,i)) == 0:
				section_arr[j] =  0
			else:
				section_arr[j] = (arr[j]//(pow(10,i)))%10
		arr = CountingSort(section_arr,arr)

	return arr


def CountingSort(arr,origin_arr):
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
		sortedarr[sumCount[arr[index]]-1] = origin_arr[index]
		sumCount[arr[index]] = sumCount[arr[index]] - 1
		index = index-1
	return sortedarr

# l = [111,222,1,2,4,44,55,90]
l = []
f = open("./IntegerArray.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break

print(RadixSort(l))