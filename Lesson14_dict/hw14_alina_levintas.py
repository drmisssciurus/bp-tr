"""
Task 1
def substring_index(text:str, pattern:str)->int:
    for i in range(len(text)-len(pattern)+1):# 0123456 45
        if text[i:i+len(pattern)]==pattern:
            return i
    return -1


Task 2:
add elements in dict in loop


Task 3: Count character frequency in a string
Description:


Write a function char_freq(s: str) -> dict that returns a dictionary where:


key — a character


value — how many times it appears in the string.


Task 4: Invert a dictionary (swap key ↔ value)
Description:
1-11 2-22 3-33 -> 33-3 22-2 11-1
Given a dictionary with unique values, write a function that swaps keys and values.


Task 5****: Invert a dictionary (swap key ↔ value)
Description:
1-1 2-1 3-1 4-2 5-2 6-2 -> 1-[1,2,3] 2-[4,5,6]
Given a dictionary with not unique values, write a function that swaps keys and values.
"""

# Task 1
def substring_index(text:str, pattern:str)->int:
	if not isinstance(text, str) or not isinstance(pattern, str):
		print(f"Error: text or pattern must be str, got {type(text).__name__} {type(pattern).__name__}")
		return -1
	for i in range(len(text)-len(pattern)+1):# 0123456 45
		if text[i:i+len(pattern)]==pattern:
			return i
	return -1

# Task 2

def add_elem_in_loop(keys:list, items:list)->dict:
	new = {'fruit': 'orange'}
	if not isinstance(keys, list) or not isinstance(items, list):
		print(f"Error: keys or items must be list, got {type(keys).__name__} {type(items).__name__}")
		return new
	if len(keys) == 0 or len(items) == 0:
		print("Error: keys or items cannot be empty")
		return new
	if len(keys) != len(items):
		print("Error: keys and items must be equal")
		return new
	for i in range(len(keys)): #0 1 2
		new[keys[i]] = items[i]
	return new

list0 = ["apple", "tomato", "cherry"]
list1 = ["fruit", "vegetable", "berrie"]

print(add_elem_in_loop(list1, list0))


# Task 3
def char_count(string: str, char: str) -> int:
	result = string.lower().count(char.lower())
	return result

def char_freq(s: str)->dict or str:
	new_dict = {}
	if not isinstance(s, str):
		print(f"Error: s must be str, got {type(s).__name__}")
		return new_dict
	if not s:
		print("Error: s is empty str")
		return new_dict

	for ch in s:
		count = char_count(s, ch)
		new_dict[ch] = count
	return new_dict

print(char_freq('apple'))

# Task 4
def invert_dict(some_dict:dict):
	if not isinstance(some_dict, dict):
		error = "Error: wrong type"
		return error
	new_dict = {}
	for key, elem in some_dict.items():
		new_dict[elem] = key
	return new_dict

user = {
	"name": "Anna",
	"age": 25,
	"city": "Haifa"
}

print(invert_dict(user))


