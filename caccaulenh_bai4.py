# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:52:45 2024

@author: Nguyen Minh Kha 
"""

# Nhập vào số nguyên dương N có 2 chữ số 
N = int(input("Nhập số nguyên dương có 2 chữ số N: "))

# Kiểm tra điều kiện để đảm bảo N là số nguyên dương có 2 chữ số
if N < 10 or N > 99:
    print("Vui lòng nhập một số nguyên dương có 2 chữ số.")
else:
    # Tách các chữ số của N
    chuc = N // 10          # Chữ số ở hàng chục 
    don_vi = N % 10         # Chữ số ở hàng đơn vị

    # Tính tổng các chữ số
    tong = chuc + don_vi

    # In kết quả ra màn hình
    print(f"Tổng các chữ số của {N} là: {chuc} + {don_vi} = {tong}")
