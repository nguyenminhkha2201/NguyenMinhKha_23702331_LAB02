# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:40:21 2024

@author: Nguyen Minh Kha 
"""

# Nhập ký tự chữ thường từ người dùng
ky_tu_thuong = input("Nhập ký tự chữ thường: ")

# Kiểm tra xem đầu vào có phải là một ký tự chữ thường không
if len(ky_tu_thuong) == 1 and ky_tu_thuong.islower():
    # Chuyển ký tự chữ thường thành chữ hoa
    ky_tu_hoa = ky_tu_thuong.upper()
    
    # In ký tự chữ hoa ra màn hình
    print(f"Ký tự chữ hoa tương ứng là: {ky_tu_hoa}")
else:
    print("Đầu vào không hợp lệ. Vui lòng nhập một ký tự chữ thường duy nhất.")
