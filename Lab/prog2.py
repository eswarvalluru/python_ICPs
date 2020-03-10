dict1={'A': 30 , 'B':40 ,'C' :20}
dict2={'e': 60 , 'd':10 ,'f' :90}
dict2.update(dict1)
for key, value in sorted(dict2.items(), key=lambda item: item[1]):
    print(key,':' ,value)
