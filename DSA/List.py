# datas structure in python 
# 1 lists
# A list is an ordered collection of items that can be changed.
# Properties of List
# ✔ Ordered (index exists)
# ✔ Mutable (can change)
# ✔ Allows duplicates
# ✔ Can store mixed data types
my_list = [1,2,3,4,5]
print(my_list)
# Accessing list items
print(my_list[0]) # Output: 1

# Modifying list items
my_list[0] = 10

print(my_list)

# Adding items to a list
my_list.append(6)
print(my_list)

# Removing items from a list
my_list.remove(3)
print(my_list)

# List slicing
print(my_list[1:4]) # Output: [2, 4, 5]