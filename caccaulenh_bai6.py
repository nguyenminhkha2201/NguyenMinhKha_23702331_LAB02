# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:22:41 2024

@author: Nguyen Minh Kha 
"""

from datetime import datetime

# Nhập vào năm sinh từ người dùng
nam_sinh = int(input("Nhập năm sinh của bạn: "))

# Lấy năm hiện tại
nam_hien_tai = datetime.now().year

# Tính tuổi
tuoi = nam_hien_tai - nam_sinh

# In kết quả ra màn hình
print(f"Bạn sinh năm {nam_sinh} vậy bạn {tuoi} tuổi.")
