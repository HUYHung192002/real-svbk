# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.

def is_perpect(a):
    sum = 0
    for i in range(1,a-1):
        if a % i == 0:
            sum += i
    if sum == a:
       return('True')
    else:
        return('False')


k = int(input('Test n:'))
is_perpect(k)