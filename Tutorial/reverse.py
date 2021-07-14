a = [1,2,3]

print(list(reversed(a)))
for num in reversed(a):
    print(num)

print(a)

a.reverse()

print(a)

a = "1234"
print(a[1:])
print(a[:])
print(a[::1])
print(a[::2])
print(a[::-1])
print(a[::-2])


a = False

if not a:
    print("yes")
else:
    print("No")

# 1 1 2 2 3
#
# 1 2 3 ? ?

a = "1234"
for i, num in enumerate(a):
    print(i, num)


print(max([1,2,3]))