# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:04:37 2024

@author: Nguyen Minh Kha 
"""

# Nhập giờ, phút, giây từ người dùng
gio = int(input("Nhập số giờ (h): "))
phut = int(input("Nhập số phút (p): "))
giay = int(input("Nhập số giây (s): "))

# Tính tổng số giây
tong_giay = gio * 3600 + phut * 60 + giay

# In kết quả ra màn hình
print(f"Tổng số giây là: {tong_giay}")
