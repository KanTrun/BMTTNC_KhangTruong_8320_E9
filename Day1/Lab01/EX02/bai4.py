def dauCuoiTuple(tuple_data):
    first_Element = tuple_data[0]
    last_Element = tuple_data[-1]
    return first_Element, last_Element

input_tuple = eval(input("Nhap TUPLE: (1, 2, 3): "))
first, last = dauCuoiTuple(input_tuple)

print("Dau tuple: ", first)
print("Cuoi tuple: ", last)