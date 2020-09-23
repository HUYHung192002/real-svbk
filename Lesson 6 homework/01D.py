
#Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict



my_dict = {
    'a' : 213,
    'b' : 545,
    'c' : 3434
    }
Max = max(my_dict.keys(),key=lambda k: my_dict[k])
Min = min(my_dict.keys(),key=lambda k: my_dict[k])

print(f'Maximun value:{my_dict[Max]}')
print(f'Minimum value:{my_dict[Min]}')
