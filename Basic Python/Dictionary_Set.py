#  Dictionary & Set

printSpacing = "--------"

print("")
print("Dictionary & Set")
print(printSpacing, "Dictionary", printSpacing)
print("")

# Dictionaries are used to store data values in key:value pairs

# They are unordered, mutable(changeable) & don’t allow duplicate keys

info = {
    "name": "Pradip Patel",
    "age": 30,
    "sex": "Male",
    "is_Adult": True,
    "subject": ("swift", "Objective-C", "Python", "C"),
    "topics": ("dict", "set"),
    12: "12"
}

print(info)

# Dictionaries Key only store Data Type Value, Not Dict and List set key. Because it is mutable. 

print("Info type of class is =>", type(info))

print("Name is =", info["name"])

print("If dict has not right key it will be error, Like Ex.")
print("info['Name']")


info["name"] = "Pradip R Patel"

print(info)

emptyDict = {}

print("Empty Dict =", emptyDict)


print("")
print(printSpacing, "Nested Dictionaries", printSpacing)
print("")

student = {
    "name": "Pradip Patel",
    "score": [
            {
                "subject": "chem",
                "marks": "98"
            },
            {
                "subject": "physics",
                "marks": "94"
            },
            {
                "subject": "maths",
                "marks": "84"
            }
        ]
}

print("student =", student)

print("")
print(printSpacing, "Dictionaries Methods", printSpacing)
print("")


ky = student.keys()         #returns all keys

print("student.keys() =")
print(ky)
print("keys() return type is =>", type(ky), end="\n\n")

vl = student.values()       #returns all keys

print("student.values() =")
print(vl)
print("values() return type is =>", type(vl), end="\n\n")

tup = student.items() #returns all (key, val) pairs as tuples

print("student.items() =")
print(tup)
print("items() return type is =>", type(tup), end="\n\n")

vl = student.get("key") #returns the key according to value
print("student.get('key') =")
print(vl)
print("get() return type is =>", type(vl), end="\n\n")

# Dictionary get value use direct bracket to get() function is safe for Error/Crash issue.

vl = student.get("name")
print("student.get('name') =")
print(vl)
print("get() return type is =>", type(vl), end="\n\n")

avrg = (98 + 94 + 84) / 3

nDct = {"score": f"{avrg} %"}       # f use string in variable Bracket. 
student.update(nDct) #inserts or update the specified items to the dictionary

student.update({'name': "Patel"}) #only update fileld dictionary allowed.
                            
print(student)


print("")
print(printSpacing, "Set", printSpacing)
print("")

# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable and all data types.
# Set is never store mutable value Like Dictionary & List.
# Set is mutable but in set store value is immutable.

nums = { 1, 2, 3, 4 }

print("Set nums =", nums)

set2 = { 1, 2, 2, 2 }

#repeated elements stored only once, so it resolved to {1, 2}
print("Set set2 =", set2)

null_set = set() #empty set syntax

print("Empty Set =", null_set)

print("null_set type of class is =>", type(null_set))

# Set Methods

collection = set()

print("collection Value is =", collection)

print("collection add() methods")
collection.add(1)
print("collection Value is =", collection)

collection.add(2)
print("collection Value is =", collection)

collection.add(3)
print("collection Value is =", collection)

collection.add(2)
print("collection Value is =", collection)

collection.add("1")    # set string in "1" or intger 1 or float 1.0 are all same hash value. then it can not add.
print("collection Value is =", collection)

collection.add((1,2))
print("collection Value is =", collection)

# collection.add([1,2,3])
# unhashable type: 'list'
# List has unhashable value, but list in every items has hashable value.

collection = {1,2,3,4,"A","B", 'a', 'b', 4, 2}
print("collection Value is =", collection)

# collection.remove(element) # collection.remove(item)
# removes the element a set

print("\n\ncollection remove() methods")


collection.remove('a')
print("collection Value is =", collection)

collection.remove('b')
print("collection Value is =", collection)

if 2 in collection:         # or you can write          len(collection.intersection({2})) == 1
    collection.remove(2)
    print("collection Value is =", collection)
    
if 'a' in collection:         # or you can write          len(collection.intersection({'a'})) == 1
    collection.remove('a')
    print("collection Value is =", collection)
else:
    print("'a' is not in collection")

collection.add("e")
collection.add("d")
collection.add("f")
collection.add("saf")

print("collection Value is =", collection)

print("\n\ncollection pop() methods")

# set.pop() #removes a random value
pV = collection.pop()
print("Collection pop value is random =", pV)
print("collection Value is =", collection)

pV = collection.pop()
print("Collection pop value is random =", pV)
print("collection Value is =", collection)

print("\n\ncollection clear() methods")

# collection.clear() # empties the set
collection.clear()
print("collection after clear() Value is =", collection)


collection = {1, 2, 3, 4, 'b', 'A', 'a', 'B'}

print("collection Value is =", collection)

print("intersection =", collection.intersection({3, 5, 6}))

print("union =", collection.union({3, 4, 5, 6}))


