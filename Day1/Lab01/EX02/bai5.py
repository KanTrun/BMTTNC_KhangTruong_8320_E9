def soLanXuatHien(list):
    count = {}
    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

input_str = input("Nhap danh sach cac chu: ")
word_list = input_str.split()

soLan = soLanXuatHien(word_list)
print("So Lan Xuat Hien: ", soLan)