# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:22:54 2024

@author: Nguyen Minh Kha 
"""

# Nhập số nguyên từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra số và in giá trị tương ứng
if 0 <= so <= 9:
    if so == 0:
        print("Khong")
    elif so == 1:
        print("Mot")
    elif so == 2:
        print("Hai")
    elif so == 3:
        print("Ba")
    elif so == 4:
        print("Bon")
    elif so == 5:
        print("Nam")
    elif so == 6:
        print("Sau")
    elif so == 7:
        print("Bay")
    elif so == 8:
        print("Tam")
    elif so == 9:
        print("Chin")
else:
    print("Khong doc duoc")
