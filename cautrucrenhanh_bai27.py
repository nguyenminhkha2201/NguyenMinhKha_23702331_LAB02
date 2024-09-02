# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:39:42 2024

@author: Nguyen Minh Kha 
"""

import math

# Nhập loại hình từ người dùng
loai_hinh = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ").lower()

if loai_hinh == 'v':
    # Tính diện tích và chu vi của hình vuông
    canh = float(input("Nhập chiều dài cạnh của hình vuông: "))
    chu_vi = 4 * canh
    dien_tich = canh ** 2
    print(f"Chu vi của hình vuông: {chu_vi:.2f}")
    print(f"Diện tích của hình vuông: {dien_tich:.2f}")

elif loai_hinh == 'n':
    # Tính diện tích và chu vi của hình chữ nhật
    rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    dai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chu_vi = 2 * (rong + dai)
    dien_tich = rong * dai
    print(f"Chu vi của hình chữ nhật: {chu_vi:.2f}")
    print(f"Diện tích của hình chữ nhật: {dien_tich:.2f}")

elif loai_hinh == 't':
    # Tính diện tích và chu vi của hình tròn
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh ** 2
    print(f"Chu vi của hình tròn: {chu_vi:.2f}")
    print(f"Diện tích của hình tròn: {dien_tich:.2f}")

else:
    print("Loại hình không hợp lệ. Vui lòng nhập v, n hoặc t.")
