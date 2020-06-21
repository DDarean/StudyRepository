phrase = "Don't panic!"
plist = list(phrase)
print (phrase)
print (plist)


plist = plist[1:8]
plist.remove("'")
plist.insert(2,plist.pop(3))
plist.insert(4,plist.pop(5))

new_phrase =''.join(plist)
print (plist)
print(new_phrase)
