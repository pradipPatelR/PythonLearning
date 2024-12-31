#  Dictionary & Set

printSpacing = "--------"

print("")
print("Dictionary & Set")
print(printSpacing, "List", printSpacing)
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

vl = student.get("name")
print("student.get('name') =")
print(vl)
print("get() return type is =>", type(vl), end="\n\n")