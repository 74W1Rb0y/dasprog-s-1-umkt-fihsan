list1 = ['fajar', 'ihsan h', 2003, 2023]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

my_list = [10, 20, 30, 40, 50]

my_list.append(60)
my_list.extend([70, 80, 90])
my_list.insert(3, 35)

my_list.remove(20)
popped_item = my_list.pop(4)
del my_list[0]
my_list.clear()

count_30 = my_list.count(30)
index_40 = my_list.index(40)

my_list.sort()
my_list.reverse()

new_list = my_list + [100, 110]
my_list_copy = my_list.copy()

