import xlrd
import copy

def getData(file,num):
	data = xlrd.open_workbook(file)
	table = [0]*num
	info = []
	college = 0
	# table_vehicle = data.sheet_by_index(0)
	# table_material = data.sheet_by_index(1)
	# table_software = data.sheet_by_index(2)
	# table_computer = data.sheet_by_index(3)

	for i in range(num):
		table[i] = data.sheet_by_index(i)
		for j in range(table[i].nrows):
			row = [m for m in table[i].row_values(j) if m!='']

			if len(row)==1:
				college = row[0][0:row[0].find("院")+1]
			if len(row) > 1 and type(row[0])!=str:
				row.insert(0,college)
				info.append(row)

	return info

def sortedByEnglish(file,fnum,k):
	grades = getData(file,fnum)
	EngGrades = [i[:4] for i in grades]
	print(MergeSort(EngGrades,0,len(EngGrades)-1,-1)[-1:-10:-1])
	
def sortedByAll(file,fnum,k):
	grades = getData(file,fnum)

	Engrades = MergeSort(grades,0,len(grades)-1,-3)[-1:-10:-1]
	print("-----")
	calusGrades = MergeSort(grades,0,len(grades)-1,-2)[-1:-10:-1]
	print("-----")
	algbGrades = MergeSort(grades,0,len(grades)-1,-1)[-1:-10:-1]
	final = [i for i in Engrades if i in calusGrades and i in algbGrades]
	print(final)

def MergeSort(unsorted,low,high,index):
	if low<high:
		MergeSort(unsorted,low,(low+high)//2,index)
		MergeSort(unsorted,(low+high)//2+1,high,index)
		Merge(unsorted,low,high,index)
	return unsorted

def Merge(unsorted,low,high,index):
	list1 = [i for i in unsorted[low:(low+high)//2+1]]
	list2 = [i for i in unsorted[(low+high)//2+1:high+1]]
	i = 0
	j = 0
	list1.append([float("inf")]*3)
	list2.append([float("inf")]*3)
	for k in range(low,high+1):
		if list1[i][index] < list2[j][index]:
			unsorted[k] = list1[i]
			i = i+1
		else:
			unsorted[k] = list2[j]
			j = j+1
	return unsorted


sortedByAll("grades.xls",4,5)