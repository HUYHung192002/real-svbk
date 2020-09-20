dict1 = {
        'name': 'HuytNguyen',
        'study': 'Python',
        'sport': 'Basketball',
        'game': 'CS.Go'
        }

keys = ['name', 'study']
dict2 = {x: dict1[x] for x in keys}

print(dict2)
   