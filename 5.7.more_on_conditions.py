if 1 < 2 < 3:
    print('Sane')

if 1 < 2 == 3:
    print('Noes')

if 1 < 2 < 3 < 4 < 5:  # a < 2 AND 2 < 3 AND 3 < 4...
    print('yes')

if [1, 2, 3] == [1, 2, 3]:  # equality operator
    print('yes')

if [1, 2, 3] is [1, 2, 3]:  # identity operator
    print('no...')

if 2 in [1, 2, 3]:  # if value is in sequence
    print('Oh yes')


# in, not in, is, not is have all lower precedence than numerical operators

if True or True and False:  # left to right, short circuit
    print('wut')

print(True and 'lollers')  # lollers
print(False and 'lollers')  # False


s1, s2, s3 = '', 'Trondheim', 'Hammer Dance'
s = s1 or s2 or s3
print(s)  # 'Trondheim'
