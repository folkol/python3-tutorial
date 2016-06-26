words = ['cat', 'window', 'toss']

for word in words[:]:
    if word.startswith('to'):
        words.insert(0, word)

print(words)
