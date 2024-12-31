# Data Types

print("Data Types")
print("")

intA = 123
strB = "Hello"
floatC = 12.34
booleanD = True
noneE = None    # None Value or it is none type.

print("intA Value is =>", intA)
print("strB Value is =>", strB)
print("floatC Value is =>", floatC)
print("booleanD Value is =>", booleanD)
print("noneE Value is =>", noneE)

print("")

booleanD = False

print("intA Type is  =>", type(intA))
print("strB Type is  =>", type(strB))
print("floatC Type is  =>", type(floatC))
print("booleanD Type is  =>", type(booleanD))
print("noneE Type is  =>", type(noneE))

print("")

# Single Line Comment

"""

Multi Line
Comment

"""

# Types of Operators

print("Types of Operators")
print("")


# Arithmetic Operators ( + , - , *, / , % , ** )
# Relational / Comparison Operators ( == , != , > , < , >= , <= )
# Assignment Operators ( = , +=, -= , *= , /= , %= , **= )
# Logical Operators ( not , and , or )

print("Arithmetic Operators")
print("'Plus' Operators 2 + 6 =", 2 + 6)
print("'Minus' Operators 2 - 6 =", 2 - 6)
print("'Multiplication' Operators 2 * 6 =", 2 * 6)
print("'Division' Operators 6 / 2 =", 6 / 4)
print("'Modulus' Operators 6 / 2 =", 6 / 4)
print("'Exponentiation' Operators 2 ** 3 /or/ 2 * 2 * 2 =", 2 ** 3)

print("")
print("Relational / Comparison Operators")
print("'Equal' Operators 2 == 6 =", 2 == 6)
print("'Not Eqaul' Operators 2 != 6 =", 2 != 6)
print("'Less Than' Operators 2 > 6 =", 2 > 6)
print("'Greatar Than' Operators 6 < 2 =", 6 < 2)
print("'Less Than Equal to' Operators 3 >= 3 =", 3 >= 3)
print("'Greatar Than Equal to' Operators 4 <= 3 =", 4 <= 3)

print("")
print("Assignment Operators")

storeSum = 5 + 9  # 14
print("'Store' Operators for storeSum = 5 + 9 is ", storeSum)
storeSum += 6  # 20
print("'Plus Equal to' Operators for storeSum += 6 is ", storeSum)
storeSum -= 10  # 10
print("'Minus Equal to' Operators for storeSum -= 10 is ", storeSum)
storeSum *= 4  # 40
print("'Multiplication Equal to' Operators for storeSum *= 4 is ", storeSum)
storeSum /= 2  # 20.0
print("'Division Equal to' Operators for storeSum /= 2 is ", storeSum)
storeSum %= 7  # 6.0
print("'Modulus Equal to' Operators for storeSum %= 7 is ", storeSum)
storeSum **= 2  # 36.0
print("'Exponentiation Equal to' Operators for storeSum **= 2 is ", storeSum)

print("")
print("Logical Operators")

print("'not' Operators =", not True)
print("'not' Operators =", not False)
print("\n'and' Operators True and True =", True and True)
print("'and' Operators True and False =", True and False)
print("'and' Operators False and True =", False and True)
print("'and' Operators False and False =", False and False)
print("\n'or' Operators True or True =", True or True)
print("'or' Operators True or False =", True or False)
print("'or' Operators False or True =", False or True)
print("'or' Operators False or False =", False or False)

print("")
print("Type Conversion")

valueA, valueB = 1, 2.0
valueSum = valueA + valueB
print("Number Data Type float is superior")
print("valueSum = 1 + 2.0 =>", valueSum)

# a, b = 1, "2"
# sum = a + b
# Error - Can not sum integer and string

print("")
print("Type Casting")

print("")
valueA = 2
valueB = "3"

valueB = int(valueB)
valueSum = valueA + valueB
print("Integer Sum ", valueSum)

valueB = "3.6"
valueB = float(valueB)
valueSum = valueA + valueB
print("Float Sum ", valueSum)

print("")
print("Input in Python")
print("input( ) statement is used to accept values (using keyboard) from user\n")

input("Please enter value: ")
print("Input with store object in Python and it is store direct in string\n")

vlA = input("vlA is store : ")
vlB = input("vlB is store : ")

print("\nvlA & vlB Convert in float\n")

vlA = float(vlA)
vlB = float(vlB)

vlSum = vlA + vlB

print("Float Sum ", vlSum)

