def find_min_value(array:list[int])->int:
	return min(array)

arr = [1,2,3,4,5,6]
print(find_min_value(arr))

def min_value(ar:list[int])->int:
	min_=ar[0]
	for x in ar:
		if x<min_:
			min_=x
	return min_

my_list2 = [1,2,3,4,5]
print(min_value(my_list2))

