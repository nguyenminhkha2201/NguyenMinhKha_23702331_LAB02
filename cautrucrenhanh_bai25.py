# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:32:33 2024

@author: Nguyen Minh Kha 
"""

# Nhập ký tự từ người dùng
ky_tu = input("Nhập một ký tự: ")

# Kiểm tra và chuyển đổi ký tự
if ky_tu.islower():
    # Nếu ký tự là chữ thường, chuyển thành chữ hoa
    ky_tu_moi = ky_tu.upper()
elif ky_tu.isupper():
    # Nếu ký tự là chữ hoa, chuyển thành chữ thường
    ky_tu_moi = ky_tu.lower()
else:
    # Nếu không phải là chữ cái, thông báo lỗi
    ky_tu_moi = "Không phải là ký tự chữ."

# In kết quả
print(f"Ký tự sau khi đổi là: {ky_tu_moi}")
