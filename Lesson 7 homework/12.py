# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1


def find_position(a,x):
    
    b = len(a)
    for i in range(len(a)):
        if a[i] == x:
            print(i)
            
    return -1

a = [2, 123, 123, 5435, 3123]
x = 123
p = find_position(a,x)