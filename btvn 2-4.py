a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a + b < c or b + c < a or a + c < b :
    print("Ko ton tai tam giac")
elif a == b == c:
    print("Tam giac deu")
else:
     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print("Tam giac vuong")
        if a == b or b == c or c == a:
            print("tam giac vuong can")
     else:
        print("tam giac thuong")
          