import random as ran

def q1():
	totalw = 0
	avgw = 0
	weight = [None for i in range(100)]
	for i in range(100):
		weight[i] = ran.randint(1500,4000)
		#weight.append(w)

	for i in range(len(weight)):
		totalw = totalw + weight[i]
		avgw = totalw/100
	#print(weight)
	print('The avg birth weight is',avgw)
	count = 0
	totalwbelow = 0
	for i in range(len(weight)):
		if weight[i] < avgw - 500:
			totalwbelow = totalwbelow + weight[i]
			count += 1
	avgwbelow = totalwbelow/count
	print('Number of babies 500 below avgw is',count)
	print('their avg weight is {:6.1f}'.format(avgwbelow))

#qns2
def q2():
	mark = [ [None for i in range(3)] for i in range(5)]
	for i in range(len(mark)):
		for j in range(len(mark[i])):
			marks = ran.randint(1,10)
			print('enter mark {0} for student {1}'.format(j+1, i+1))
			mark[i][j] = marks
	for i in range(len(mark)):
		total = int(0)
		print('STUDENT {0}'.format(i+1))
		for j in range (len(mark[i])):
			total = total +mark[i][j]
		average = total / len(mark[i])
		print('Student {0} has an average of {1}'.format(i+1, average))
	total = int(0)
	count = int(0)
	for i in range(len(mark)):
		for j in range(len(mark[i])):
			total = total + mark[i][j]
			count += 1
	average = total/count
	print('\nGroup avg is {:1.1f}'.format(average))
#print(mark)

Maxsize = 10
numArr = [None for i in range(Maxsize)]
nlist = [6,18,31,46,52]
for i in range(5):
	numArr[i] = nlist[i]

def insert(Array, newItem):
        if Array[Maxsize-1] != None:
                print('Array is full.')
                return Array
                
        else:
                for i in range(Maxsize):
                        print(i)
                        if (Array[i] == None) or (newItem < Array[i]):
                                print(Array[i])
                                index = i
                                break
                for i in range(Maxsize - 1, index, -1):
                        Array[i] = Array [i-1]
                Array[index] = newItem
                
        return Array

numArr = insert(numArr, 10)
print(numArr)
