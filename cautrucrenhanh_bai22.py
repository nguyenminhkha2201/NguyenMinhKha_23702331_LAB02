# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:25:25 2024

@author: Nguyen Minh Kha 
"""

# Nhập hệ số a và b từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Giải phương trình bậc nhất ax + b = 0
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    # Tính nghiệm của phương trình ax + b = 0
    x = -b / a
    print(f"Phương trình có nghiệm x = {x:.2f}")
