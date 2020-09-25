# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j





def create_matrix(n,m):
    for i in range(n+1):
        for j in range(m+1):
            P = i*j
            return(f"vi tri {i} , {j} : {P}")
    


n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

create_matrix(n,m)