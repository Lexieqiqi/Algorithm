# Find the max number and the min number in one array
# Use one pair of two numbers to compare with each other and then the min compare with current min so as the max

def FindMaxAndMin(arr):
	l = len(arr)
	min = 0
	max = 0
	# even
	if l%2 == 0:
		if arr[0] < arr[1]:
			min = arr[0]
			max = arr[1]
		else:
			min = arr[1]
			max = arr[0]
		l = 2
	# odd
	else:
		min = arr[0]
		max = arr[0]
		l = 1

	# compare with each pair in the arr
	for x in range(l+1,len(arr),2):
		if arr[x]<arr[x-1]:
			if arr[x] < min:
				min = arr[x]
			if arr[x-1] > max:
				max = arr[x-1]
		else:
			if arr[x-1] < min:
				min = arr[x]
			if arr[x] > max:
				max = arr[x-1]
	return min,max

# l = [111,222,1,2,4,44,55,90]
l = []
f = open("./IntegerArray.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break
print(FindMaxAndMin(l))
print(min(l),max(l))

