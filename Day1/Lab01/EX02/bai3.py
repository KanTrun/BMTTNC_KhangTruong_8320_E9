def tupleList(list):
    return tuple(list)

input_list = input("Nhap danh sach so: ")
numbers = list(map(int, input_list.split(',')))
print("List: ", numbers)
print("Tuple FROM List: ", tupleList(numbers))