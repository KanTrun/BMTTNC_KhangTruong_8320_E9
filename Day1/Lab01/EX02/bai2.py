def daoNguocList(list):
    return list[::-1]

input_list = input("Nhap danh sach cac so: ")
numbers = list(map(int, input_list.split(',')))

listDaoNguoc = daoNguocList(numbers)
print("List sau khi dao nguoc: ", listDaoNguoc)