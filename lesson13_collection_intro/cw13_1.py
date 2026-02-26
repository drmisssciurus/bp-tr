'''
list
tuple
'''

my_tuple = (1,2,3,4,5)

my_list = [1,2,3,4,5]

print(len(my_list), len(my_tuple))
print(len(my_list), len(my_tuple))
print(id(my_tuple))
print(id(my_list))

print(my_list.count(1))
print(my_tuple.count(1))

my_list[0] = 100
print(my_list)

# my_tuple[0] = 12
# print(my_tuple)

my_list.append(1000)
print(my_list)

my_list.sort()
print(my_list)

tuple_differ_types = (1, '1', True, 78.8)
print(tuple_differ_types)

list_1 = ['222','111', 'dfjhvbfd', 'b', 'a', '123']
list_1.sort()
print(list_1)

list_1.sort(key=len)
print(list_1)

list_1.sort(key=len,reverse=True)
print(list_1)


my_old_tuple = ('222', 111, 'dfjhvbfd', 'b', 'a', '123')
print("index tuple is ",id(my_old_tuple))
my_new_list = list(my_old_tuple)
print("index list is ",id(my_new_list))
print(my_new_list)
my_new_list[0] = 12445364
my_new_list.insert(5, 3000)
print(my_new_list)

my_new_tuple = tuple(my_new_list)
print(my_new_tuple)
print("index tuple is ",id(my_new_tuple))

print(my_list)
print(my_list.pop(5))
print(my_list)
