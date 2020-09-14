n = int(input("Nhap so duong n: "))

while n < 0 or n >= 1000 :
    print("Error. Yeu cau nhap lai n")
sum = 0
while n > 0 :
    sum = sum + n % 10
    n = n // 10
print("Tong cac chu so: {}".format(sum))