# Find out the leargest element form a list whithout using max() function.
"""
h = [23,11,43,22,34,54,88,12,36,2]
t = h[0]
for i in h:
    if i>t:
        t=i
print(t)
"""
# Using max() functions...
"""
y = max(h)
print(y)
"""
My_list = [12,23,12,44,32,54,76,44,32,64]
print("The length of this list is: ", len(My_list)) # len() function helps to find out the length of a list
My_list.insert(5,64) # .insert(index,value) use to add new value or item in a particular position (index) of a list
print("Updated list after inserting 64 : ",My_list)
My_list.append(78) # .append() function can only add 1 single item (number or string) in the very last of the list
print(My_list)
foods = ["Momo","Ice-cream"]
foods.append("Fish fry") # .append() can also be used to add string to a list (a list of strings)...
print(foods)
    