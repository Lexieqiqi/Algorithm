def readFile(file):
	f = open(file)
	job_weight = []
	job_length = []
	ratio = []
	line = f.readline()
	while True:
		line = f.readline()
		if line!='':
			comb = line.strip().split(' ')
			job_weight.append(int(comb[0]))
			job_length.append(int(comb[1]))
			ratio.append(int(comb[0])/int(comb[1]))
		if not line:
			break
	return job_weight,job_length,ratio

def getMiniCompl(file):
	job_weight,job_length,ratio = readFile(file)
	# use insertion sort to sort diff 
	for i in range(1,len(ratio)):
		key = ratio[i]
		key1 = job_weight[i]
		key2 = job_length[i]
		j = i-1
		while j>=0 and ratio[j]>key:
			ratio[j+1] = ratio[j]
			job_weight[j+1] = job_weight[j]
			job_length[j+1] = job_length[j]
			j = j-1
		ratio[j+1] = key 
		job_weight[j+1] = key1
		job_length[j+1] = key2
		
		weil = [j+1]
		while j>=0 and ratio[j]==key:
			weil.append(j)
			j = j-1

		for x in weil[-2::-1]:
			k = job_weight[x]
			k1 = job_length[x]
			t = x - 1
			while t>=weil[-1] and job_weight[t]>k :
				job_weight[t+1] = job_weight[t]
				job_length[t+1] = job_length[t]
				t = t - 1
			job_weight[t+1] = k
			job_length[t+1] = k1
		
	j_len = len(job_weight)-1
	sum = job_length[j_len]*job_weight[j_len]
	while j_len >= 1:
		job_length[j_len-1] = job_length[j_len-1] + job_length[j_len]
		sum = sum + job_weight[j_len-1]*job_length[j_len-1]
		j_len = j_len -1
	return sum


print(getMiniCompl("./jobs.txt"))