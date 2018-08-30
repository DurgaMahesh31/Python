""" To Practice the typecasting Operations """
list_of_fruits = ["Apple" , "Banana" , "Orange"]
input_value = input("Enter some number:" )
print(type(input_value))
print(int(2.34))

#list_of_fruits [3]
#int("2.65")

print(int("0o1", base=8))
print(int(2.34))
print(int(0o1))

#print(help(int))

#print(help(int))

print("Given Value is:"+input_value)

class_information = [
    {"name":"xyz",
     "dob":"13/07/2017"},
    {"name":"yz",
     "dob":"12/05/2017"}
]


new_tuple = tuple(class_information)
print(type(new_tuple))
print(new_tuple)


# list(1)
# print("2nd Class information :"+ str(class_information))
#
# debug_message = "2nd Class information :%s"%(class_information)
# debug_message2 = "2nd class information:{a} {b}".format(a=10, b=20)
# debug_message3 = "{cls}nd class information".format(cls=2)
# print(debug_message3)
#
# print(debug_message)
# print(debug_message2)