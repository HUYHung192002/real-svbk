n = int(input("Nhap vao n: "))
x = float(input("Nhap gia tri x: "))

sum_1 = 1
sum_2 = 1
sum_3 = 1
i = 1
while i < n + 1 :
    sum_1 += x**i
    sum_2 += ((-1)**i)*(x**i)
    i += 1