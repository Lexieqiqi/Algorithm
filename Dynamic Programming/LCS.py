def LSC(X,Y):
	a = len(X)
	b = len(Y)
	c = [[0 for column in range(b+1)] for row in range(a+1)]
	d = [[0 for column in range(b+1)] for row in range(a+1)]

	for i in range(a):
		for j in range(b):
			if X[i] == Y[j]:
				c[i+1][j+1] = c[i][j] + 1
				d[i+1][j+1] = '\\'
			else:
				c[i+1][j+1] = max(c[i][j+1],c[i+1][j])
				if c[i+1][j+1]==c[i][j+1]:
					d[i+1][j+1] = '|'
				else:
					d[i+1][j+1] = '--'

	maxSub = []
	s = d[a][b]
	while s != 0:
		if s == '\\':
			maxSub.append(X[a-1])
			a = a-1
			b = b-1
		elif s == '--':
			b = b-1
		elif s == '|':
			a = a-1
		s = d[a][b]

	return c,''.join(maxSub[::-1])

print(LSC('ABDKfffss','CDABODgsdgsgsgs'))