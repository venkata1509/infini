set = {538,536,537,539,540,535}
set1 = {538,541,553,561,548,536}

print(type(set))
print(type(set1))

print(len(set))
print(len(set1))

set.add(551)
print(set)

# set.remove(551)
# print(set)

# set.discard(551)
# print(set)

element = set.pop()
print(element)
print(set)

union = set.union(set1)
print(union)

intersection = set.intersection(set1)
print(intersection)

difference = set.difference(set1)
print(difference)

symmetricdifference = set.symmetric_difference(set1)
print(symmetricdifference)

# for x in set:
#     print(x)