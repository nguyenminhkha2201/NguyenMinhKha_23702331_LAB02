# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:35:14 2024

@author: Nguyen Minh Kha 
"""

# Nhập số xe từ người dùng
so_xe = input("Nhập số xe (gồm 4 chữ số): ")

# Kiểm tra số xe có phải là số 4 chữ số không
if so_xe.isdigit() and len(so_xe) == 4:
    # Đếm số nút (chữ số)
    so_nut = len(so_xe)
    
    # In kết quả ra màn hình
    print(f"Số xe của bạn có {so_nut} nút.")
else:
    print("Số xe không hợp lệ. Vui lòng nhập một số nguyên dương gồm 4 chữ số.")
