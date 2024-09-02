# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:44:10 2024

@author: Nguyen Minh Kha 
"""

import random

# a) Số nguyên ngẫu nhiên từ 0 đến 100
so_nguyen_0_100 = random.randint(0, 100)
print(f"Số nguyên ngẫu nhiên từ 0 đến 100: {so_nguyen_0_100}")

# b) Số nguyên ngẫu nhiên từ 50 đến 99
so_nguyen_50_99 = random.randint(50, 99)
print(f"Số nguyên ngẫu nhiên từ 50 đến 99: {so_nguyen_50_99}")

# c) Số thực ngẫu nhiên từ -39 đến 79
so_thuc_mo_39_den_79 = random.uniform(-39, 79)
print(f"Số thực ngẫu nhiên từ -39 đến 79: {so_thuc_mo_39_den_79:.2f}")

# d) Số thực ngẫu nhiên từ -79 đến -39
so_thuc_mo_79_den_39 = random.uniform(-79, -39)
print(f"Số thực ngẫu nhiên từ -79 đến -39: {so_thuc_mo_79_den_39:.2f}")
