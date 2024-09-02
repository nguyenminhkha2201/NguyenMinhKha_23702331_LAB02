# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:31:55 2024

@author: Nguyen Minh 
"""

# In ra menu lựa chọn
print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")

# Nhận lựa chọn của người dùng
lua_chon = input("Moi nhap lua chon: ")

# In kết quả theo lựa chọn của người dùng
print("==============================")
if lua_chon == '1':
    print("Ban da chon Hu tieu.")
elif lua_chon == '2':
    print("Ban da chon Chao long.")
elif lua_chon == '3':
    print("Ban da chon Banh canh.")
elif lua_chon == '4':
    print("Ban da chon Bun rieu.")
elif lua_chon == '5':
    print("Ban da chon Pho bo.")
else:
    print("Lua chon khong hop le.")
print("==============================")
