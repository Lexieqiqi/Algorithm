# Input: array A containing the numbers 1,2,3,4,5,6 in some arbitary order

# Output: number of inversions = number of pairs(i,j) of array index with i<j , A[i]<A[j]

def Sort_and_Count(arr,length):
	if length == 1:
		return arr,0
	else:
		arr1 = arr[0:length//2]
		arr2 = arr[length//2:length]
		xarr,x = Sort_and_Count(arr1,length//2)
		yarr,y = Sort_and_Count(arr2,length-length//2)
		zarr,z = Sort_and_CountSplitInv(xarr,yarr,length)
		return zarr,x+y+z

def Sort_and_CountSplitInv(arr1,arr2,length):
	sortedarr = arr1+arr2
	arr1.append(float("inf"))
	arr2.append(float("inf"))
	i = 0
	j = 0
	inv_count = 0
	for k in range(length):
		if arr1[i]<=arr2[j]:
			sortedarr[k] = arr1[i]
			i = i + 1
		else:
			inv_count += length//2-i
			sortedarr[k] = arr2[j]
			j = j + 1
	# Inversions = []
	# for a in range(length):
	# 	if sortedarr[a] in arr2 and a<length//2:
	# 		Inversions.append([sortedarr[a],arr1[a:length//2]])
	# 	elif sortedarr[a] in arr1 and a>length//2:
	# 		Inversions.append([sortedarr[a],arr2[0:a-length//2+1]])
	#print("The sortedarr is:",sortedarr)
	return sortedarr,inv_count

# l = [1,3,5,7,2,4,6,8,7,5,78,20,11,4]
# print(Sort_and_Count(l,len(l)))

l = []
f = open("./IntegerArray.txt")
while True:
	line = f.readline()
	if line!='':
		l.append(int(line.strip('\n')))
	if not line:
		break
print(Sort_and_Count(l,len(l)))