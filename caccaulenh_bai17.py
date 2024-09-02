# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:11:37 2024

@author: Nguyen Minh Kha 
"""

# Nhập ba số nguyên từ người dùng
so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))
so3 = int(input("Nhập số nguyên thứ ba: "))

# Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = max(so1, so2, so3)
so_nho_nhat = min(so1, so2, so3)

# In kết quả ra màn hình
print(f"Số lớn nhất là: {so_lon_nhat}")
print(f"Số nhỏ nhất là: {so_nho_nhat}")
