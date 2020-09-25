# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str


def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
print(reverse('asdasdasdasOCN'))