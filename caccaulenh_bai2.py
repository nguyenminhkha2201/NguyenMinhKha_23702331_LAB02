# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:35:22 2024

@author: Nguyen Minh Kha 
"""

2# Nhập vào 2 số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính tổng
tong = a + b

# Tính hiệu
hieu = a - b

# Tính tích
tich = a * b

# Tính thương và làm tròn đến 3 chữ số sau dấu thập phân
# Chú ý cần xử lý trường hợp chia cho 0
if b != 0:
    thuong = a / b
    thuong = round(thuong, 3)
else:
    thuong = 'Không thể chia cho 0'

# In kết quả ra màn hình
print("Tổng của a và b là:", tong)
print("Hiệu của a và b là:", hieu)
print("Tích của a và b là:", tich)
print("Thương của a và b là:", thuong)
