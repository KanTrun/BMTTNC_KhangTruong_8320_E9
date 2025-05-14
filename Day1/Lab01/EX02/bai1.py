def tong_Chan(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhap danh sach so: ")
numbers = list(map(int, input_list.split(',')))

tong = tong_Chan(numbers)
print("Tong so chan: ", tong)