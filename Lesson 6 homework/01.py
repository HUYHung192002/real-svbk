my_dict = {
    1: 231,
    45: 2312,
    'w': 23311,
    'rtjerkt': 232
    }
max = 0
min = 0
for i in my_dict:
    for j in my_dict:
        if my_dict[i] < my_dict[j]:
            max = my_dict[j]
print("Max: {}".format(max))


for i in my_dict:
    for j in my_dict:
        if my_dict[i] > my_dict[j]:
            min = my_dict[j]
print("Min: {}".format(min))