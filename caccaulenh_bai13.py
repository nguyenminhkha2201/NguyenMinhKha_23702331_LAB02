# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:46:09 2024

@author: Nguyen Minh Kha 
"""

# Nhập ngày, tháng, năm sinh từ người dùng
ngay = int(input("Nhập ngày (dd): "))
thang = int(input("Nhập tháng (mm): "))
nam = int(input("Nhập năm (yyyy): "))

# Xuất ngày/tháng/năm (dd/mm/yyyy)
print(f"a) Ngày/tháng/năm: {ngay}/{thang}/{nam}")

# Xuất ngày/tháng/năm (dd/mm/yy)
nam_rut_gon = nam % 100  # Lấy 2 chữ số cuối của năm
print(f"b) Ngày/tháng/năm: {ngay}/{thang}/{nam_rut_gon:02d}")

# Xuất năm/tháng/ngày (yyyy/mm/dd)
print(f"c) Năm/tháng/ngày: {nam}/{thang}/{ngay}")

# Chuyển đổi ngược lại từ định dạng yyyy/mm/dd về dd/mm/yyyy
# Chia năm thành 2 phần
nam_rut_gon = nam % 100  # Lấy 2 chữ số cuối của năm
# Xuất lại theo định dạng dd/mm/yyyy
print(f"Ngược lại: Ngày/tháng/năm: {ngay}/{thang}/{nam}")
