#Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file


f_file = open('file_check02.txt','a', encoding= 'cp1252')

f_file.writelines('Absolutely!!!')
