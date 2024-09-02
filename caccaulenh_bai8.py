# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:29:37 2024

@author: Nguyen Minh Kha 
"""
# Nhập cân nặng (kg) từ người dùng
can_nang = float(input("Nhập cân nặng của bạn (kg): "))

# Nhập chiều cao (m) từ người dùng
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))

# Tính chỉ số BMI
bmi = can_nang / (chieu_cao ** 2)

# In kết quả ra màn hình
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")

# Đưa ra phân loại BMI
if bmi < 18.5:
    print("Bạn thuộc nhóm thiếu cân.")
elif 18.5 <= bmi < 24.9:
    print("Bạn thuộc nhóm cân nặng bình thường.")
elif 25 <= bmi < 29.9:
    print("Bạn thuộc nhóm thừa cân.")
else:
    print("Bạn thuộc nhóm béo phì.")

