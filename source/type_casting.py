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

output = subprocess.getoutpur("ipconfig")
logger.info(output)
logger.info(output.splitlines())



ip_addr = "127.0.0.1"
# list_of_octal = ip_addr.split(".")
# logger.info(list_of_octal)
new_ip_addr =ip_addr.replace("127","10")
# logger.info(list_of_octal)
# logger.info(".".join(list_of_octal))
logger.info(new_ip_addr, ip_addr)


logger.info(ip_addr.ljust(20,"x"))
logger.info(ip_addr.rjust(20,'x'))
logger.info(ip_addr.center(20,'x'))
logger.info(ip_addr.zfill(20))

list_of_employees.sort(key=lambda item : item['emp_id'])

list_of_employees = [
    {"emp_id":34,
     "emp_name":"xx ab"},
    {"emp_id":2,
     "emp_name":"yy ca"},
    {"emp_id":1,
     "emp_name":"zz dc"}
]   # 34, 2, 1  # 1, 2, 34



list_of_employees.sort(key=lambda emp_data: emp_data['emp_id'])
logger.info(list_of_employees)


list_of_employees = [
    {"emp_id":34,
     "emp_name":"xx ab"},
    {"emp_id":2,
     "emp_name":"yy ca"},
    {"emp_id":1,
     "emp_name":"zz dc"}
]   # 34, 2, 1  # 1, 2, 34

# sort:
#     for item in list_of_employees:
#         key_to_compare(item)

def key_to_compare_dict(item):
    logger.info(item)
    return item['emp_id']

# list_of_employees

list_of_employees.sort(key=lambda emp_data: emp_data['emp_id'])
list_of_employees.sort(key=key_to_compare_dict)
logger.info(list_of_employees)

# dict.keys() -> [key1, key2,...]
# dict.values() -> [ value1, value2,... ]
# dict.items() -> [ (key1, value1), (key2, value2) ...]
logger.info(emp_data.keys())
logger.info(emp_data.values())
logger.info(emp_data.items())
emp_data["emp_id"] = 12345
logger.info(emp_data.items())

emp_data["emp_id"] = 1234
logger.info(emp_data.items())
new_data = {"emp_name":"new_xx", "emp_id":1234,"emp_dob":"12/05/1990"}
emp_data.update(new_data)
logger.info(emp_data.items())
logger.info(emp_data)
logger.info(emp_data.pop("emp_id"))  # value of removed key
logger.info(emp_data)
logger.info(emp_data.popitem())  # (key,value)
logger.info(emp_data)
emp_data.clear()
logger.info(emp_data)
# help(emp_data.popitem)
#----------- Sets ---------------------

logger.info(dir(set))
data_set = set()
logger.info(data_set)
data_set.add(123)
data_set.add(243)
logger.info(data_set)

logger.info(dir(set))
data_set = set()
logger.info(data_set)
data_set.add(123)
data_set.add(243)
logger.info(data_set)
new_data_set = {23, 124, 123, 24}
data_set.update(new_data_set)
logger.info(data_set)

logger.info(dir(set))
data_set = set()
logger.info(data_set)
data_set.add(123)
data_set.add(243)
logger.info(data_set)
new_data_set = {23, 124, 123, 24}
data_set.update(new_data_set)
logger.info(data_set)
logger.info(data_set.difference(new_data_set))  # data_set - new_data_set
logger.info