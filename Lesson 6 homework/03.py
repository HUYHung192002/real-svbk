y_dict = {
    1: 123,
    2: 435,
    4: 435,
    324: 234,
    9: 123
    }
result = {}
for key, val in my_dict.items():
    if val not in result.values():
        result[key] = val

   
print(result)
