names = ["Ben","Jan"]


grades=[1,2]
#dict {(key, value)}
names_and_grades={"Ben":1,"Jan":2}
print(names_and_grades)

names_and_grades.update({"Pia":3})
print(names_and_grades)

names_and_grades["Jan"] = 1
print(names_and_grades)

names_and_grades.pop("Jan")
print(names_and_grades)

#keys
for k in names_and_grades.keys():
    print(k)

#Values
for v in names_and_grades.values():
    print(v)

#key,Values
for v in names_and_grades.items():
    print(v)


for k,v in names_and_grades.items():
    print(k,v)

if "Jan" in  names_and_grades:
   print("Jan is present!")
else:
    print("Jan is not present")
