# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h

def body_mass_index(m, h):
    BMI = m / (h**2)
    return(f"BMI:{BMI}")

def bmi_information(m, h):
    BMI = m / (h**2)
    if BMI < 18.5 :
        return("Thieu can")
    elif BMI >= 18.5 and BMI <= 24.9:
        return("Binh thuong")
    elif BMI > 25 and BMI < 29.9:
        return("Thua can")
    else:
        print("Beo phi")
body_mass_index(70, 1.75)
bmi_information(70, 1.75)