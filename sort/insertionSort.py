# Insertion Sort

'''
choose the second element as the key element
if the number before the key is larger than the key, then put the key number into the right prosition before
Note: the series before the key are sorted.
'''

def insertionSort(unsorted):
	for x in range(1,len(unsorted)):
		key = unsorted[x]
		i = x-1
		while i >= 0 and unsorted[i] > key:
			unsorted[i+1] = unsorted[i]
			i = i-1
		unsorted[i+1]=key
	return unsorted

test_list = [2,8,1,9,22,19,89,3]		
print(insertionSort(test_list))