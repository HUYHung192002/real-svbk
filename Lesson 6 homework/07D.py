dict1 = {
        'name': 'HuytNguyen',
        'study': 'Python',
        'sport': 'Basketball',
        'game': 'CS.Go'
        }

keys = ['name', 'study']
dict2 = {x: dict1[x] for x in keys}

print(dict2)
# Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
# Ví dụ:
#     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#     keys = ["name", "salary"]
#     Output: {'name': 'Kelly', 'salary': 8000}