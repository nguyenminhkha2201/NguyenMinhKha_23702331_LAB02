# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:35:30 2024

@author: Nguyen Minh Kha 
"""

# Nhập ba số từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

# Sử dụng một biến phụ để sắp xếp
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# In các số theo thứ tự tăng dần
print(f"Các số theo thứ tự tăng dần: {a}, {b}, {c}")
