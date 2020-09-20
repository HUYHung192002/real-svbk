my_dict = {
    1: 231,
    45: 2312,
    'w': 23311,
    }

multi = 1
for value in my_dict.values():
    multi *= value

print(multi)