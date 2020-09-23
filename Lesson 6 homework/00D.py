
#Bài 00: Viết chương trình tính tích value của các phần tử trong một dict

my_dict = {
    1: 231,
    45: 2312,
    'w': 23311,
    }

multi = 1
for value in my_dict.values():
    multi *= value

print(multi)