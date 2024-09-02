# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:24:58 2024

@author: Nguyen Minh Kha 
"""
import math

# Nhập bán kính của hình tròn từ người dùng
ban_kinh = float(input("Nhập bán kính của hình tròn: "))

# Tính chu vi
chu_vi = 2 * math.pi * ban_kinh

# Tính diện tích
dien_tich = math.pi * (ban_kinh ** 2)

# In kết quả ra màn hình
print(f"Chu vi của hình tròn là: {chu_vi:.2f}")
print(f"Diện tích của hình tròn là: {dien_tich:.2f}")

