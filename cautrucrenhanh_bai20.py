# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:20:24 2024

@author: Nguyen Minh Kha 
"""

# Nhập 3 số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

# Giả định rằng số lớn nhất là a
lon_nhat = a

# So sánh với b
if b > lon_nhat:
    lon_nhat = b

# So sánh với c
if c > lon_nhat:
    lon_nhat = c

# In số lớn nhất ra màn hình
print(f"Số lớn nhất là: {lon_nhat}")
