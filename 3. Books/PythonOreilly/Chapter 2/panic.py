phrase = "Don't panic!"
plist = list(phrase)
print (phrase)
print (plist)

delete= ['D',"'",'i','c','!']

for bukva in delete:
    plist.remove(bukva)

plist.pop()
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))

new_phrase =''.join(plist)
print (plist)
print(new_phrase)
