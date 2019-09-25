def CutRud(p,n):
	r = [0]*(n+1)
	s = [0]*(n+1)
	for j in range(1,n+1):
		q = float("-inf")
		for i in range(1,j+1):
			if q < p[i-1] + r[j-i]:
				q = p[i-1]+r[j-i]
				r[j] = q
				s[j] = i
	return r,s

print(CutRud([1,5,8,9,10,17,17,20,24,30],10))
