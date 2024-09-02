# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:57:50 2024

@author: Nguyen Minh Kha 
"""

# Nhập hai số a và b từ người dùng
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Tính các phần của biểu thức
a_cubed_root = a ** (1/3)  # Căn bậc ba của a
b_cubed_root = b ** (1/3)  # Căn bậc ba của b
ab_cubed_root = (a * b) ** (1/3)  # Căn bậc ba của a*b

# Tính giá trị của biểu thức
numerator = (a + b) / (a_cubed_root + b_cubed_root)
denominator = ab_cubed_root / (a_cubed_root - b_cubed_root) ** 2

result = numerator - denominator

# In kết quả ra màn hình
print(f"Giá trị của biểu thức là: {result:.4f}")
