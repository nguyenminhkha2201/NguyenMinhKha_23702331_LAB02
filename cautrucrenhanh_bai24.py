# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:30:20 2024

@author: Nguyen Minh Kha 
"""

# Nhập giờ, phút, giây từ người dùng
gio = int(input("Nhập giờ (0-23): "))
phut = int(input("Nhập phút (0-59): "))
giay = int(input("Nhập giây (0-59): "))

# Kiểm tra tính hợp lệ
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian không hợp lệ.")
