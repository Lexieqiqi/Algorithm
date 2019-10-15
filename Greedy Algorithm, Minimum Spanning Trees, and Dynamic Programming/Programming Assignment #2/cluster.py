def swap(arr,x,y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr

def QuickSort(vertice_sorted,edge_sorted,low,high):
	if low<high:
		pivot = edge_sorted[low]
		i = low+1
		j = low+1
		while j <= high:
			if edge_sorted[j]<pivot:
				swap(edge_sorted,j,i)
				swap(vertice_sorted,j,i)
				i = i+1
			j=j+1
		swap(edge_sorted,low,i-1)
		swap(vertice_sorted,low,i-1)
		QuickSort(vertice_sorted,edge_sorted,low,i-2)
		QuickSort(vertice_sorted,edge_sorted,i,high)
	return vertice_sorted,edge_sorted

def getGraph(file):
	f = open(file)
	line = f.readline()
	v_num = int(line.split(' ')[0])
	vertice = []
	vertices = {}
	cost = []
	while True:
		line = f.readline()
		if line!='':
			info = line.strip().split(' ')
			vertice.append(info[0]+","+info[1])
			cost.append(int(info[2]))
		if not line:
			break
	vertices.fromkeys(vertice,0)
	for i in range(len(vertice)):
		vertices[vertice[i]] = cost[i]
	return v_num,vertice,vertices

def clustering(file,k):
	v_num, vertice, vertices = getGraph(file)
	# sort the egde in increasing order
	vertice_sorted = []
	edge_sorted = []
	for i in vertice:
		vertice_sorted.append(i)
		edge_sorted.append(vertices[i])
	vertice_sorted,edge_sorted = QuickSort(vertice_sorted,edge_sorted,0,len(edge_sorted)-1)

	print(edge_sorted)
	maximum_space = 0
	clusters = v_num
	# Union Find data structure to initiate the vertices
	ufVertices = UF(v_num+1)
	# Iterator till it contains 4 clusters
	for i in range(len(edge_sorted)):
		v1 = int(vertice_sorted[i].split(',')[0])
		v2 = int(vertice_sorted[i].split(',')[1])
		# tell if they can form a cycle
		if not ufVertices.find(v1,v2):
			ufVertices.union(v1,v2)
			clusters = clusters-1
			print("The clusters is :",clusters)
			if clusters==3:
				maximum_space = edge_sorted[i]
				break
	return maximum_space

class UF:
	# An implementation of union find data structure

	def __init__(self,N):
		self._id = list(range(N))
		self._count = N
		for i in range(N):
			self._id[i] = i

	def find(self,p,q):
		return self.getRoot(p) == self.getRoot(q)

	def count(self):
		return self._count

	def union(self,p,q):
		rootP = self.getRoot(p)
		rootQ = self.getRoot(q)
		for i in range(1,self._count):
			if self._id[i] == rootQ:
				self._id[i] = rootP

	def getRoot(self,p):
		return self._id[p]




print(clustering("./clustering.txt",4))