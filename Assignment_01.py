# Python Practice Questions: Lists and Sets
# Lists
# 1.  List Creation: Create a list containing the first 10 natural numbers using a loop.
My_list = [1]

for i in range(2,11):
        My_list.insert(i,i)
print(My_list)
# 2. Positive Filter: Given a list of integers, create a new list containing only positive numbers.
My_list = [11,-2,33,4,54,23,-6,43,-9,87,6,-7]
print(My_list)
for j in My_list:
        if j<0:
            My_list.remove(j)
print(My_list)
# 3. Element Swap: Swap the first and last elements of a list.
The_list = [23,11,43,22,34,54,88,12,36,2]
print(The_list)
first_element = The_list[0]
last_element = The_list[len(The_list)-1]
The_list.remove(first_element)
The_list.append(first_element)
The_list.remove(last_element)
The_list.insert(0,last_element)
print(The_list)
# 4. Count Occurrences: Count how many times a specific element appears in a list.
future_blood = ["Gov. school","LMG or LMB","Private school","Summit school","LMG or LMB","CBSE school","LMG or LMB","BCM International","LMG or LMB","St. Xavier","LMG or LMB","Gov. school"]
count = 0
for i in future_blood:
       if i == "LMG or LMB":
            count += 1
print(count)
# 5. List Concatenation: Concatenate two lists without using the + operator.
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list0 = [9,10,11,12,13]
list1.extend(list2)
print(list1)
list3 = list1 + list0
print(list3)

# 1. Set Creation: Create a set of vowels from a given string.
school = "LA_MARTINIERES_SCHOOL"
vowels = {"A"}
vowels.clear()
for i in school:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels.add(i)
print(vowels)

