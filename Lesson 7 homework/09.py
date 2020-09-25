# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str

def change_str(s):
    test = []
    for i in s:
        if i.islower():
            test.append(i.upper())
        elif i.isupper():
            test.append(i.lower())
        else:
            test.append(i)
    return ''.join(test)

a = 'Test case 1'

print(change_str(a))