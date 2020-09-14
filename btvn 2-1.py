a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
delta = b**2 - 4*a*c
if a == 0:
	if b == 0:
		if c == 0:
			print("PT co vo so nghiem")
		else : print("PT vo nghiem")
	else : 
		x = -c / b 
		print( "PT co nghiem x = {}".format(x) )
elif delta == 0:
	x = -b / (2 * a)
	print("PT co nghiem kep x = {}".format(x))
elif delta > 0:
	x1 =  -b + sqrt(delta) / (2 * a)
	x2 =  -b - sqrt(delta) / (2 * a)
	print("PT co 2 nghiem phan biet x1 = {}, x2 = {}".format(x1, x2))
else:
	print("PT vo nghiem")