# Manhattan Problems 
# Find the longest path to visit
row = [[0,0,0,0,0],[0,3,2,4,0],[0,3,2,4,2],[0,0,7,3,4],[0,3,3,0,2],[0,1,3,2,2]]
col = [[0,0,0,0,0],[0,1,4,4,5],[0,0,6,4,6],[0,2,5,5,8],[0,4,2,2,5],[0,3,1,1,3]]

def init(row,col):
	path = [[] for j in range(len(row))]
	nodes = [[0 for i in range(len(col))] for j in range(len(row))]
	for i in range(1,len(col)):
		for j in range(1,len(row)):
			nodes[i][j] = max(nodes[i-1][j]+col[j][i-1],nodes[i][j-1]+row[i][j-1])
			if nodes[i][j] == nodes[i-1][j]+col[j][i-1]:
				path[i].append("|")
			else:
				path[i].append("->")
			#print(nodes[i][j])
			#print(path)
	print(path)
	return nodes



nodes = init(row,col)
print(nodes)


