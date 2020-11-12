vowels = set('aeiou')
word = input("word: ")
found = []

i = vowels.intersection(sorted(set(list(word))))
print(i)
