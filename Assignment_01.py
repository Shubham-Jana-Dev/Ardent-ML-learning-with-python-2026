# Python Practice Questions: Lists and Sets
# Lists
# 1.  List Creation: Create a list containing the first 10 natural numbers using a loop.
My_list = [1]

for i in range(2,11):
        My_list.insert(i,i)
print(My_list)
# 3 Positive Filter: Given a list of integers, create a new list containing only positive numbers.
My_list = [11,-2,33,4,54,23,-6,43,-9,87,6,-7]
print(My_list)
for j in My_list:
        if j<0:
            My_list.remove(j)
print(My_list)