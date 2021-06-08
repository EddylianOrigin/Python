list_a=[10,20,30]
list_b=["Jan","Peter","Max"]

for val_a, val_b in zip(list_a, list_b):
    print(val_a, val_b)

print("\n")

for i in range(len(list_a)):
    print(i, list_a[i])

print("\n")

for i, val in enumerate(list_a):
    print(i, val)
