#Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:

   input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
   output = {}

   for item_dict in input:
       name = item_dict['item']
       amount = item_dict['amount']
       if item in output:
           output[item] += amount
           else:
               output[item] = amount

print(output)