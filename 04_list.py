#-------------------first block--------------------->
# Initialize of list ---------->
# my_list = ["banana", "apple", "orange"]
# this_list = ["banana", "apple", "orange", "apple"]

# print(my_list)
# print(this_list)
# print(my_list[0])
# print(len(my_list))

# for x in my_list:
#     print(x)


#----------various list ------->
# list1 = ["a", 12, 2.4, True]
# list2 = ["apple", {"price": 10}, "5kg"]
# list3 = list(("banana", "apple"))

# print(list1)
# print(list2)
# print(list3)




#-------------------second block--------------------->
# Access list items ---------->
# my_list = ["apple", "banana", "orange", "mango", "lichi"]

# print(my_list[1])
# print(my_list[-1])
# print(my_list[1:3])
# print(my_list[2:])
# print(my_list[:4])
# print(my_list[-4:-1])

# for x in my_list:
#     print(x)

# if "apple" in my_list:
#     print("Yes")
# else:
#     print("No")





#-------------------third block--------------------->
# Change list items ------------>

# my_list = ["apple", "banana", "orange", "mango", "lichi"]

# my_list[2] = "pineapple"
# print(my_list)

# my_list[1:2] = ["pineapple", "lemon"]
# print(my_list)

# my_list.insert(1, "pineapple")
# print(my_list)

# my_list.insert(len(my_list), "pineapple")
# print(my_list)








#-------------------fourth block--------------------->
# Add list items --------------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]

# my_list.append("pineapple")
# print(my_list)

# my_list.insert(3, "pineapple")
# print(my_list)



# new_list = ["pineapple", "lemon"]
# my_list.extend(new_list)
# print(my_list)

# my_tuple = ("pineapple", "lemon")
# my_list.extend(my_tuple)
# print(my_list)






#-------------------fifth block--------------------->
# Remove list items ------------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]

# my_list.remove("banana")
# print(my_list)

# x = my_list.pop(1)
# print(x)
# print(my_list)


# x = my_list.pop()
# print(x)
# print(my_list)

# del my_list[2]
# print(my_list)

# my_list.clear()
# print(my_list)





#-------------------sixth block--------------------->
# Loop lists --------------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]


# for fruit in my_list:
#     print(fruit)



# for fruit in range(len(my_list)):
#     print(my_list[fruit])


# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i+=1






#-------------------seventh block--------------------->
# List comprehension ---------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]


# [print(x) for x in my_list]

# new_list = [x for x in my_list]
# print(new_list)


# new_list = [x for x in my_list if "a" in x]
# print(new_list)


# new_list = [x for x in my_list if x != "apple"]
# print(new_list)





#-------------------eighth block--------------------->
# Sort list ---------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]
# number_list = [80, 100, 50, 70, 60]

# my_list.sort()
# print(my_list)



# number_list.sort()
# print(number_list)

# number_list.sort(reverse=True)
# print(number_list)






#-------------------ninth block--------------------->
# Copy list ---------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]

# new_list = my_list.copy()
# print(new_list)


# new_list = list(my_list)
# print(new_list)





#-------------------tenth block--------------------->
# Join Lists ---------->

# my_list = ["apple", "banana", "orange", "mango", "lichi"]
# another_list = ["pineapple", "lemon"]


# final_list = my_list + another_list
# print(final_list)


# my_list.extend(another_list)
# print(my_list)



# for x in another_list:
#     my_list.append(x)
# print(my_list)




#-------------------eleventh block--------------------->
# List Methods ---------->

# my_list = ["apple", "banana", "orange", "mango", "apple", "lichi"]


# my_list.reverse()
# print(my_list)

# print(my_list.count("apple"))


