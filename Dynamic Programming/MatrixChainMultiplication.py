def MatrixChainMulti(p):
	n = len(p) - 1
	m = [[0 for col in range(n)] for row in range(n)]
	s = [[0 for col in range(n)] for row in range(n)]

	for l in range(2,n+1):
		for i in range(1,n-l+2):
			j = i+l-1
			m[i-1][j-1] = float("inf")
			for k in range(i,j):
				q = m[i-1][k-1]+m[k][j-1]+p[i-1]*p[k]*p[j]
				if q < m[i-1][j-1]:
					m[i-1][j-1] = q
					s[i-1][j-1] = k

	return s,m

print(MatrixChainMulti([30,35,15,5,10,20,25]))