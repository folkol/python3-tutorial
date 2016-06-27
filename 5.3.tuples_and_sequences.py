t1 = 12345, 'Hello', ['n', 'i', 'n', 'j', 'a']
print(t1)
print(t1[0])
t2 = 1, (2, 3)
print(t2)
print((1, 2, 3) is (1, 2, 3))
print((1, 2, 3) == (1, 2, 3))

t3 = t1, t2
print(t3)
# t3[0] = 1  # tuples do not support item assignment...

t4 = 1,
print(t4)
t5 = ()
print(t5)

t6 = (1)  # NOT a tuple...
print(t6)

t = 12345, 54321, 'Hello!'  # Tuple 'packing'
print(t)
a, b, c = t  # Sequence 'unpacking'
print(a, b, c)
a, b, c = [1, 2, 3]
print(a, b, c)

# a, b, c = [1, 2, 3, 4]  # Too many values to unpack...
# print(a, b, c)


t = 'Hello',  # Tailing command, singleton
print('Len: ', len(t))
