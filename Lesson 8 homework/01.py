#Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng

f_read = open('file_check.txt', 'r', encoding = 'cp1252')

n = int(input('Nhap n:'))

for i in range(0,n):
    print(f_read.readlines(i))
