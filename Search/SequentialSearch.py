def sequentialSearch(array, value) :
	for i in range(len(array)) :
		if array[i] == value:
			return i
	return False

numList = [11,30,4,14,22,9,24,5]
res = sequentialSearch(numList, 3)
print(res)
