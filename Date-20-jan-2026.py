# l 01
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
# l 02
print("\n\n----Understanding the len(Name_list) Function----\n\n")
My_list = [12,23,12,44,32,54,76,44,32,64]
print("The length of this list is: ", len(My_list)) # len() function helps to find out the length of a list

print("\n\n----Understanding the .insert(index,value) Function----\n\n")
My_list.insert(5,64) # .insert(index,value) use to add new value or item in a particular position (index) of a list
print("Updated list after inserting 64 : ",My_list)

print("\n\n----Understanding the .append(value) Function----\n\n")
My_list.append(78) # .append() function can only add 1 single item (number or string) in the very last of the list
print(My_list)

foods = ["Momo","Ice-cream"]
foods.append("Fish fry") # .append() can also be used to add string to a list (a list of strings)...
print(foods)
# l 03
print("\n\n----Understanding the .remove(value) Function----\n\n")
My_list.remove(23) # .remove() is used for remove a specific Element for a list
print(My_list)

print("\n\n----Implementing loops in the list Function----\n\n")
for i in My_list:
    print(i) # we can print all elemets of a list by using loops.
D = {45,32,44,31,42,56} # This is a Set (uses curly braces)
print(D)

print("\n\n----Implementing type conversion from set to list in the list Function----\n\n")
lis = list(D) # Casting/Converting the Set into a List
print(lis)

print("\n\n----Implementing logical operation between 2 lists the list Function----\n\n")
a = [3,4,6,2,43,54,11]
b = [5,7,8,3,6,23,43,11]
print("\n---OR OPERATION---\n")
l_OR = a or b 
print(l_OR) 
print("\n---AND OPERATION---\n") 
l_AND = a and b 
print(l_AND)

print("\n\n----Implementing Arithmatic operation between 2 lists the sets Function----\n\n")
print("\n---Subtraction---\n") 
Set1 = {3,4,6,2,43,54,11}
Set2 = {5,7,8,3,6,23,43,11}
S_sub = Set1 - Set2
print("Set1 - Set2 = ",S_sub)
rev_s_sub = Set2 - Set1
print("Set2 - Set1 = ",rev_s_sub)

print("\n\n----Implementing logical operation between 2 lists the Sets Function----\n\n")
print("\n---OR OPERATION---\n")
Se_OR = Set1 or Set2
print(Se_OR) 
print("\n---AND OPERATION---\n") 
Se_AND = Set1 and Set1
print(Se_AND)

print("\n\n----Implementing bitwise operation between 2 lists the Sets Function----\n\n")
print("\n---XOR OPERATION---\n")
Se_XOR = Set1^Set1
print(Se_XOR)