# find out 5 from the list [12,334,5,56,7,453,6,67]
import numpy as np
def finding_element():
    arr = np.array([12,334,5,56,7,453,6,67])
    terget = np.where(arr == 5)
    print(terget)
# Print the shape of a list

def print_shape():
    arr1 = np.array([12,23,34,45,55,67,14,46])
    print(arr1.shape)
# print_shape()

def print_found_group_of_elements():
    arr2 = np.array([11,23,12,22,45,65,78,98,76,56,35,49,59,27,44,1,4,7,9,3,78,6])
    smaller = np.where(arr2<10)
    print(smaller)
# print_found_group_of_elements()

# Sort the list by numpy.
def sort_by_numpy():
    arr2 = np.array([11,23,12,22,45,65,78,98,76,56,35,49,59,27,44,1,4,7,9,3,78,6])
    sorted_list = np.sort(arr2)
    print(sorted_list)
# sort_by_numpy()

# Sort the list in reversed order.
def sort_by_numpy_in_reversed_order():
    arr2 = np.array([11,23,12,22,45,65,78,98,76,56,35,49,59,27,44,1,4,7,9,3,78,6])
    sorted_list_reversed = np.sort(arr2)[::-1]
    print(sorted_list_reversed)
# sort_by_numpy_in_reversed_order()

# Concatenate 2 lists.
def concatenation_of_two_lists():
    prev_list = np.array([10,20,30,40])
    second_list = ([100,200])
    marged_list = np.concatenate((prev_list,second_list))
    print(marged_list)
# concatenation_of_two_lists()

# Filter out the elements (>=5 and <=15) from a list.
def filter_out_element():
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    the_elements = arr[(arr>=5)&(arr<=15)]
    print(the_elements)
filter_out_element()