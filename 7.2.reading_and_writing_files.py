f = open('corpus.txt')
print(f.readlines())
f.close()

f = open('corpus.txt', 'r')
print(f.readlines())
f.close()

f = open('garbage.txt', 'w')
print('lol', file=f)
f.close()
f = open('garbage.txt', 'w')
print('lol', file=f)
f.close()
f = open('garbage.txt', 'r')
print(f.read())
f.close()

f = open('garbage.txt', 'w')
print('lol', file=f)
f.close()
f = open('garbage.txt', 'a')
print('lol', file=f)
f.close()
f = open('garbage.txt', 'r')
print(f.read())
f.close()
