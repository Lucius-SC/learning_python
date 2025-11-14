#sai nên fix lại v1.1
# Duyệt từng ký tự → đếm từng loại → cộng lại. => dùng for 
# char.isalpha(); char.isdigit(); char.isspace()
loc_du_lieu = input("Nhập chuỗi bất kỳ: ")
space = 0
words = 0
special = 0
for char in loc_du_lieu:
    if char.isspace():
        space += 1
    elif char.isdigit() or char.isalpha():
        words += 1
    else:
        special += 1
print(f"Space: {space} \n Words: {words} \n Special: {special}")