# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:52:46 2024

@author: Nguyen Minh Kha 
"""

# Nhập vào giờ, phút và giây theo định dạng hh:mm:ss
thoi_gian = input("Nhập thời gian theo định dạng hh:mm:ss: ")

# Tách giờ, phút và giây từ chuỗi nhập vào
try:
    # Tách chuỗi theo dấu ":"
    gio, phut, giay = map(int, thoi_gian.split(':'))

    # Kiểm tra điều kiện để đảm bảo giờ, phút và giây hợp lệ
    if (0 <= gio < 24) and (0 <= phut < 60) and (0 <= giay < 60):
        # Tính tổng số giây
        tong_giay = gio * 3600 + phut * 60 + giay

        # In kết quả ra màn hình
        print(f"Tổng số giây là: {tong_giay}")
    else:
        print("Giờ, phút hoặc giây không hợp lệ.")
except ValueError:
    print("Định dạng thời gian không hợp lệ. Vui lòng nhập theo định dạng hh:mm:ss.")
