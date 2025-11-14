# exercise 1
"""Viết một chương trình Python:
Cho người dùng nhập 1 chuỗi bất kỳ.
Chương trình trả về:
- Số khoảng trắng trong chuỗi
- Số từ trong chuỗi
- Số ký tự không phải chữ cái và không phải số
In kết quả ra màn hình theo format:
Space: <so_khoang_trang>
Words: <so_tu>
Special: <so_ky_tu_dac_biet>"""
"""
loc_du_lieu = input("Nhập chuỗi bất kỳ: ")
space = loc_du_lieu.count(" ")
words = len(loc_du_lieu.split())
special = (loc_du_lieu.count("") - (space + words))
print(f"Space: {space} \n Words: {words} \n Special: {special}")
"""
#sai nên fix lại v1.1
# Duyệt từng ký tự → đếm từng loại → cộng lại. => dùng for 
# char.isalpha(); char.isdigit(); char.isspace()
"""
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
"""
# vẫn sai chỗ đếm từ, cần đếm số từ chứ không phải số ký tự là chữ hoặc số
"""
words = len(loc_du_lieu.split())
print(f"Space: {space} \n Words: {words} \n Special: {special}")
"""
# fix v1.2 hoàn chỉnh
loc_du_lieu = input("Nhập chuỗi bất kỳ: ")
space = 0
special = 0
for char in loc_du_lieu:
    if char.isspace():
        space += 1
    elif not (char.isdigit() or char.isalpha()):
        special += 1
words = len(loc_du_lieu.split())
print(f"Space: {space} \n Words: {words} \n Special: {special}")

# v1.3 nâng cao
s = input("Nhập chuỗi bất kỳ: ")
space = 0
special = 0
words = 0

for ch in s:
    if ch.isspace():
        space += 1
# đếm special (không phải chữ/số/space)
for ch in s:
    if not (ch.isalpha() or ch.isdigit() or ch.isspace()):
        special += 1

# đếm từ thủ công
in_word = False
for ch in s:
    if not ch.isspace() and not in_word:
        words += 1
        in_word = True
    elif ch.isspace():
        in_word = False

print(f"Space: {space}\nWords: {words}\nSpecial: {special}")
