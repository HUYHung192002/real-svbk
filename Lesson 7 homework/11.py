
# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy

def fibo(n):
    if n <= 2:
        return 1
    else: 
        return fibo(n-1) + fibo(n-2)

n = int(input("Nhap so: "))

print(f'so fibo thu {n} la {fibo(n)}')