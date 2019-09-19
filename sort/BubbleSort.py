# Bubble sort
 
def BubbleSort(arr):
	for i in range(len(arr)):
		for j in range(0,len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j] 
	return arr


l = [2,45,111,32,45,3,5,6,2,89,3]

# l = []
# f = open("./IntegerArray.txt")
# while True:
# 	line = f.readline()
# 	if line!='':
# 		l.append(int(line.strip('\n')))
# 	if not line:
# 		break
print(BubbleSort(l))