
# Strings

# concatenation
print("")
print("Strings")
print("\tBasic Operations")
print("\n\t\t•Concatenation")

vlA, vlB = "Hello", "Program"
vlSum = vlA + vlB
print("\t\t\tConcatenation two object => ", vlSum)

print("\n\t\t•length of str")
print("\t\t\tLength of vlSum => ", len(vlSum))


print("")
print("------------------------------------------------\n")
print("Indexing")

print("A\tp\tn\ta\t_\tC\to\tl\tl\te\tg\te\n")
print("0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\n\n")

str = "Apna_College"

print("str[0] =", str[0])
print("str[1] =", str[1])

print("\nstr[0] = 'B' #not allowed\n")
# str[0] = 'B' #not allowed
# String is Immutable in Python 
# You can not change characted direct index, you can replace of charactet to charactet

print(f"A New Str is print = {str}") # f use string in variable Bracket. 



print("")
print("------------------------------------------------\n")
print("Slicing")

# str[ 1 : 4 ] is “pna”
print(str)
print("str[ 1 : 4 ] = ", str[1:4])

# str[ : 4 ] is same as str[ 0 : 4]
print("str[ : 4 ] = ", str[:4])
print("str[ 0 : 4 ] = ", str[0:4])

# str[ 1 : ] is same as str[ 1 : len(str) ]
# len(str) or higher get full string
print("str[ 1 : ] = ", str[1:])
print("str[ 1 : len(str) ] = ", str[1:len(str)])


print("")
print("------------------------------------------------\n")
print("Slicing Negative Index")

print("A\tp\tp\tl\te\n")
print("-5\t-4\t-3\t-2\t-1\n\n")

str = "Apple"
print(str)

# str[ -4 : -1 ] is “ppl”
print("str[ -4 : -1 ] =", str[ -4 : -1 ])


print("")
print("------------------------------------------------\n")
print("String Functions")

print("i\t \ta\tm\t \ta\t \tc\to\td\te\tr\t.\n")
print("0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\n\n")

str = "i am a coder."

print(str)
print('str.endswith("er.") = ', str.endswith("er.")) #returns true if string ends with substr
print('str.endswith("am") = ', str.endswith("am")) #returns false if string ends with substr

print('str.capitalize() = ', str.capitalize()) #capitalizes 1st char and return new string
print("str.upper() =", str.upper()) #upper case char and return new string
print("str.lower() =", str.lower()) #lower case char and return new string

print('str.replace("am", ">AM<") = ', str.replace("am", ">AM<")) #replaces all occurrences of old with new and return new string

print('str.find("am") = ', str.find("am")) #returns 1st index of 1st occurrence

print('space char count\tstr.count(" ") = ', str.count(" ")) #counts the occurrence of substr/char in string


print('')
print("\n------------------------------------------------\n")
print("Conditional Statements")

newStr = input("Find a number even or odd number. Number = ")

if (int(newStr) % 2 == 0):
    print(newStr, "number is Even.")
elif (int(newStr) % 2 == 1):
    print(newStr, "number is Odd.")
else:
    print("newStr", newStr, "is not number.")
# end if

print('')
