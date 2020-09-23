my_dict = 'Stringing'
count = {}
for i in my_dict:
    if i in count: 
        count[i] += 1
    else:
        count[i] = 1
print(count)
# Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String