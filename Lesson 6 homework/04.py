 #Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict

my_dict = {
    1: 213,
    21: 123,
    43: 12,
    2: 21,
    24: 254
    }
x = sorted(my_dict)

print(x[-3:])