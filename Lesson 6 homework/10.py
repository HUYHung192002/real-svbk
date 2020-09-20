string = ' Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản '
str = string.split(" ")

count={}
for i in str:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
 
print(count)