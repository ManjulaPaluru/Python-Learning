
a = "abcbac"
print(a)

b = []
b.extend(a)
print(b)

c = {}
index = 0
for char in b:
    # print(f" => {c}")
    if char in c:
        c[char].append(index)
    else:
        c[char] = [index]
    index = index + 1

print(c)

dictionary = {}
index = 0
for char in b:
    if char in dictionary:
        dictionary[char].append(index)
    else:
        dictionary[char] = [index]
    index = index + 1

print(dictionary)

