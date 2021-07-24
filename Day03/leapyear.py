year = int(input("Masukkan tahun: "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} Tahun kabisat")
    elif year % 400 == 0:
        print(f"{year} Tahun kabisat")
    else:
        print(f"{year} Bukan kabisat")
else:
    print(f"{year} Bukan kabisat")