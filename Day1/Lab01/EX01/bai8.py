def chiaHet5(soNhiPhan):
    soThap = int(soNhiPhan, 2)
    if soThap % 5 == 0:
        return True
    else:
        return False

chuoiSoNhiPhan = input("Nhap chuoi nhi phan: ")
soNhiPhan_list = chuoiSoNhiPhan.split(',')
soChiaHet5 = [so for so in soNhiPhan_list if chiaHet5(so)]

if len(soChiaHet5) > 0:
    ketQua = ','.join(soChiaHet5)
    print("Cac so chia het 5: ", ketQua)
else:
    print("Cha co so nao chia het cho 5")