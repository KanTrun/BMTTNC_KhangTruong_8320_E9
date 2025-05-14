soGioLam = float(input("Nhap so gio lam moi tuan: "))
luongGio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gioTieuChuan = 44
gioVuotChuan = max(0, soGioLam - gioTieuChuan)
tongLuong = gioTieuChuan * luongGio + gioVuotChuan * luongGio * 1.5
print(f'Tong luong: {tongLuong}')