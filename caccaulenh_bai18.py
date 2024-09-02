# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:14:25 2024

@author: Nguyen Minh 
"""

def convert_to_seconds(hours, minutes, seconds):
    """Chuyển đổi giờ, phút, giây thành tổng số giây."""
    return hours * 3600 + minutes * 60 + seconds

def convert_to_hms(total_seconds):
    """Chuyển đổi tổng số giây thành giờ, phút, giây."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

# Nhập giờ, phút, giây của giờ thứ nhất
h1 = int(input("Nhập giờ thứ nhất: "))
m1 = int(input("Nhập phút thứ nhất: "))
s1 = int(input("Nhập giây thứ nhất: "))

# Nhập giờ, phút, giây của giờ thứ hai
h2 = int(input("Nhập giờ thứ hai: "))
m2 = int(input("Nhập phút thứ hai: "))
s2 = int(input("Nhập giây thứ hai: "))

# Chuyển đổi giờ, phút, giây thành giây
seconds1 = convert_to_seconds(h1, m1, s1)
seconds2 = convert_to_seconds(h2, m2, s2)

# Cộng và trừ giây
sum_seconds = seconds1 + seconds2
diff_seconds = abs(seconds1 - seconds2)

# Chuyển đổi kết quả trở lại giờ, phút, giây
sum_hms = convert_to_hms(sum_seconds)
diff_hms = convert_to_hms(diff_seconds)

# In kết quả
print(f"Tổng giờ: {sum_hms[0]} giờ {sum_hms[1]} phút {sum_hms[2]} giây")
print(f"Hiệu giờ: {diff_hms[0]} giờ {diff_hms[1]} phút {diff_hms[2]} giây")
