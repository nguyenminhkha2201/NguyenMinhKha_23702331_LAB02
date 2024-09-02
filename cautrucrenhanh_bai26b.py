# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:36:39 2024

@author: Nguyen Minh Kha 
"""

# Nhập số nguyên N từ người dùng
N = input("Nhập một số nguyên: ")

# Chuyển số thành danh sách các chữ số
danh_sach_chu_so = list(N)

# Sắp xếp danh sách các chữ số
danh_sach_chu_so.sort()

# Chuyển danh sách các chữ số trở lại thành chuỗi số
so_sap_xep = ''.join(danh_sach_chu_so)

# In kết quả
print(f"Số có các chữ số theo thứ tự tăng dần: {so_sap_xep}")
