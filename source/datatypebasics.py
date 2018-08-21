""" This module is to practise data types"""
# to comment out the code select the line of code and ctrl + /

name = "Python"
print(name)
print(name[0])
print(name[-1])

a = 20
print(a) # 20
print(type(a)) # <class 'int' >
b = a
print(b) # 20
print(type(b)) # < class 'int' >

print(id(a), id(b)) # 111 111
print(a is b)  # True

print("====== Changing the object for b ======")
b = "python"
print(a)  # 20
print(b)  # python
print(type(b)) # < class 'str'>
print(id(a), id(b)) # 111 222
print(a is b)     # False

# ================== Sequential data type ==================== #
name = "python2example"
print(name)      # python2example
print(name[1])   # y
print(name[2])   # t
print(name[1], name[-5])  # y, y
print(name[4], name[-2])  # o, o
print("emptyCharacter:%s"   % name[6])
print("empty")
print(name[7])
# ===================Immutable Modification and deletion data not supported ============= #
#print("deletion not supported" )
#name[1] = 'e'
#del name[0]
#del name
#print(name)

# ======================= Mutable Modification and deletion data in Object ============ #
list_of_accounts = [ "Mahesh", "Suresh", "Naresh" ]

print(list_of_accounts[0])
list_of_accounts[0] = 23456
print(list_of_accounts[0])
del list_of_accounts[2]
print(list_of_accounts)

# ==================== Unordered data =============================== #
score_data = {"Mahesh": 199,
               "Suresh": 99,
               "Naresh": 49}

print(score_data)
print(score_data["Mahesh"])
del score_data["Naresh"]
print(score_data)

