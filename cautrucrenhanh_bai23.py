# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:26:34 2024

@author: Nguyen Minh Kha 
"""

import math

# Nhập hệ số a, b và c từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra điều kiện để giải phương trình bậc hai
if a == 0:
    print("Đây không phải là phương trình bậc hai.")
else:
    # Tính discriminant (delta)
    delta = b**2 - 4*a*c
    
    # Biện luận theo giá trị của delta
    if delta > 0:
        # Hai nghiệm thực phân biệt
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có hai nghiệm thực phân biệt: x1 = {x1:.2f} và x2 = {x2:.2f}")
    elif delta == 0:
        # Một nghiệm thực kép
        x = -b / (2 * a)
        print(f"Phương trình có một nghiệm thực kép: x = {x:.2f}")
    else:
        # Hai nghiệm phức
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print(f"Phương trình có hai nghiệm phức: x1 = {real_part:.2f} + {imaginary_part:.2f}i và x2 = {real_part:.2f} - {imaginary_part:.2f}i")
