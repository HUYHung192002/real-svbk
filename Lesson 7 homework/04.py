# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False

def is_prime(a):
    test = 0
    for i in range(1, a+1):
        if a % i == 0:
            test += 1
    if test > 2:
        return('False')
    else:
        return('True')



k = int(input('Nhap so:'))
is_prime(k)