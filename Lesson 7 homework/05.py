# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str

def count_upper_lower(a):
    upper = 0
    lower = 0
    for i in a:
        if i >= 'a' and i <= 'z':
            lower += 1
        if i >= 'A' and i <= 'Z':
            upper += 1
    return(f'Upper:{upper}')
    return(f'Lower:{lower}')


a = str(input('Nhap vao day:'))
count_upper_lower(a)