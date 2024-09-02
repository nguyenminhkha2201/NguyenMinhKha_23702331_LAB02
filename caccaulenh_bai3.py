# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:48:17 2024

@author: Nguyen Minh Kha 
"""

# Nhập vào 2 số nguyên dương từ người dùng
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Kiểm tra điều kiện đầu vào để đảm bảo a và b đều là số nguyên dương
if a <= 0 or b <= 0:
    print(" Nhập số nguyên dương cho cả a và b: ")
else:
    # Tính phần nguyên và phần dư
    phan_nguyen = a // b
    phan_du = a % b

    # In kết quả ra màn hình
    print("Phần nguyên của phép chia a chia cho b là: ", phan_nguyen)
    print("Phần dư của phép chia a chia cho b là: ", phan_du)
