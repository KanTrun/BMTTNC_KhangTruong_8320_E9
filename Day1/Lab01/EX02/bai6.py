def xoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_Dict = {'a': 2, 'b': 1, 'c': 3, 'd': 4}
key_to_del = 'b'
result = xoaPhanTu(my_Dict, key_to_del)
if result:
    print("Phan tu da xoa tu DICT:", my_Dict)
else:
    print("Phan tu khong tim thay de xoa")