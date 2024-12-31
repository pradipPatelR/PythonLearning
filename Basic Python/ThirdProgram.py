
#  List & Tuple

printSpacing = "--------"

print("")
print("List & Tuple")
print(printSpacing, "List", printSpacing)
print("")
# A built-in data type that stores set of values

# It can store elements of different types (integer, float, string, etc.)

marks = [87, 64, 33, 95, 76]            #marks[0], marks[1]..

student = ["Karan", 85, "Delhi"]        #student[0], student[1]..

student[0] = "Arjun"        #allowed in python

print(type(student))

sLen = len(student) #returns length In Int

print("student Array Length", sLen)


# List is Mutable In Python
# You can not change characted direct index, you can replace of charactet to charactet


# List Slicing

print("")
print(printSpacing, "List Slicing", printSpacing)

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# aList[ 1 : 4 ] is [2, 3, 4]
print(aList)
print("str[ 1 : 4 ] = ", aList[1:4])

# aList[ : 4 ] is same as aList[ 0 : 4]
print("aList[ : 4 ] = ", aList[:4])
print("aList[ 0 : 4 ] = ", aList[0:4])

# aList[ 1 : ] is same as aList[ 1 : len(str) ]
# len(aList) or higher get full list
print("aList[ 1 : ] = ", aList[1:])
print("aList[ 1 : len(aList) ] = ", aList[1:len(aList)])


print("\n")
print(printSpacing, "List Slicing Negative Index", printSpacing)
print("")

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("1\t2\t3\t4\t5\t6\t7\t8\t9\n")
print("-9\t-8\t-7\t-6\t-5\t-4\t-3\t-2\t-1\n\n")

print(aList)

# aList[ -4 : -1 ] is [6, 7, 8]
print("aList[ -4 : -1 ] =", aList[ -4 : -1 ])


# List Slicing

print("\n\n")
print(printSpacing, "List Methods", printSpacing, end="\n\n")

aList = [2, 1, 3]

print(aList, "\n")
# aList.insert( idx, element ) #insert element at index
print("aList.insert(2, 5)")
aList.insert(2, 5)
print(aList, "\n")

print("aList.append(4)")
aList.append(4) #adds one element at the end
print(aList, "\n")

print("aList.sort()")
aList.sort() #sorts in ascending order inside order, it is not return new value
print(aList, "\n")

print("aList.sort(reverse=True)")
aList.sort(reverse=True) #sorts in descending order
print(aList, "\n")

print("aList.reverse()")
aList.reverse() #reverses list
print(aList, "\n")


aList = ["2", "1", "3", "1"]

print("aList.remove(1), 1 is Element not index")
aList.remove("1") #removes first occurrence of element
aList.remove("1")

print(aList, "\n")


print("aList.pop(1), 1 is index => ", end=" ")
remSt = aList.pop(1) #removes element at idx
print(remSt)

print(aList, "\n\n")

print(printSpacing,printSpacing,printSpacing,printSpacing, sep="", end="\n\n")
print(printSpacing, "Tuples", printSpacing, end="\n\n")

str = """
Tuples is a built-in data type that lets us create immutable sequences of values.
"""

print(str)

tup = (87, 64, 33, 95, 76) #tup[0], tup[1]..

print("Tupple Values of is:", tup)
print("Tupple Type of is:", type(tup))
# print(type(student))

#       tup[0] = 43 #NOT allowed in python
print("tup[0] = 43 #NOT allowed in python")

tup1 = ()
tup2 = (1)          # You Can't write tuppe with out comma, either wise element type
tup3 = (1,)         # Tupple is alway write with comma with one value
tup4 = (1, 2, 3)

print("tup1 = ()")
print("Type is:", type(tup1))
print("tup2 = (1)")
print("Type is:", type(tup2))
print("tup3 = (1,)")
print("Type is:", type(tup3))


print(printSpacing, "Tuple Methods", printSpacing)

tup = (7, 2, 1, 3, 1, 5, 9, 7, 1, 3, 1)

# tup.index(element) #returns index of first occurrence
print("tup.index(element) #returns index of first occurrence")

# tup.count(element) #counts total occurrences tup.count(1) is 4
print("tup.count(element) #counts total occurrences tup.count(1) is 4")

cnt = tup.count(1) #counts total occurrences tup.count(1) is 4
print("tup.count(1) =", cnt)

idx = tup.index(3)
print("tup.index(3) =", idx)

# tup.index(value: Any, start: SupportsIndex = 0, stop: SupportsIndex = sys.maxsize, /) -> int
print("Index parameter")
print("tup.index(value: Any, start: SupportsIndex = 0, stop: SupportsIndex = sys.maxsize, /) -> int")

idx = tup.index(3, idx+1)
print("next index of tup.index(3) =", idx)


