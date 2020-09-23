# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict 

my_dict2= {
    1: 23,
    44: 213
    }
my_dict1 = {
    1: 23,
    44: 213,
    12: 231,
    43: 77
    }

for (key, value) in set(my_dict1.items()) & set(my_dict2.items()):
    print('%s: %s ' % (key, value))