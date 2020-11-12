paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    print('\t', char)
print('\n')

paranoid_android_2 = "Marvin, the Paranoid Android"
letters_2 = list(paranoid_android_2)

for char_2 in letters_2[:6]:
    print('\t', char_2)
for char_2 in letters_2[-7:]:
    print('\t'*2, char_2)
for char_2 in letters_2[12:20]:
    print('\t'*3, char_2)
