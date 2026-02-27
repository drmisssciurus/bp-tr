'''
enumerate
for in nums: -> element iteration
for i in range(): -> index iteration
for i, n in enumerate(): -> i-index,  n-elements
'''

def sum_of_odds(nums:list[int])->int:
	# animal-> primate->monkey type(chita)->monkey ==primate
	#isinstance chita[animal, primate, monkey]
	if not isinstance(nums, list):
		print(f"Error: nums must be list[int], got {type(nums).__name__}")
		return -1
	res=0
	for  i, n in enumerate(nums):
		if not isinstance(n,int) or isinstance(n,bool):
			print(f"Error: nums[{i}] must be int, got {type(n).__name__}")
			return -1
		if n%2:#11%2->1 10%2->0
			res+=n
	return res


array = [9,12,3, -9, 11, 2, 16, 1]
# print(sum_of_odds(array))
# ar =list(0)
# print(sum_of_odds(array))
# print(sum_of_odds(10))
# array = [9,12,3, -9, 11, 2, 16, True]
print(sum_of_odds(array))

def max_value(nums:list[int])->int:
	if not isinstance(nums, list):
		print(f"Error: nums must be list[int], got {type(nums).__name__}")
		return -1
	if len(nums)==0:
		print(f"Error: cannot fins empty list")
	max_=nums[0]
	for i, n in enumerate(nums):
		if not isinstance(n,int) or isinstance(n,bool):
			print(f"Error: nums[{i}] must be int, got {type(n).__name__}")
			return -1
		if n > max_:
			max_=n
	return max_

print(max_value(array))

def sum_of_odds_index(nums:list[int])->int:
	if not isinstance(nums, list):
		print(f"Error: nums must be list[int], got {type(nums).__name__}")
		return -1
	res=0
	for  i, n in enumerate(nums):
		if not isinstance(n,int) or isinstance(n,bool):
			print(f"Error: nums[{i}] must be int, got {type(n).__name__}")
			return -1
		if i%2:#11%2->1 10%2->0
			res+=n
	return res

print(sum_of_odds_index(arrayv ))