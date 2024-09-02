# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:18:16 2024

@author: Nguyen Minh Kha 
"""

# Nhập 4 số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

# Giả định rằng số nhỏ nhất là a
nho_nhat = a

# So sánh với b
if b < nho_nhat:
    nho_nhat = b

# So sánh với c
if c < nho_nhat:
    nho_nhat = c

# So sánh với d
if d < nho_nhat:
    nho_nhat = d

# In số nhỏ nhất ra màn hình
print(f"Số nhỏ nhất là: {nho_nhat}")
