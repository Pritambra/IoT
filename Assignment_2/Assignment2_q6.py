# Concatenate two lists in the following order by using list comprehension
# Input:- list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

list1 = ["Hello", " take"]
list2 = [" Dear", " Sir"]

list3 = []
list3.append(list1[0]  + list2[0])
list3.append(list1[0]  + list2[1])
list3.append(list1[1]  + list2[0])
list3.append(list1[1]  + list2[1])

print(list3)