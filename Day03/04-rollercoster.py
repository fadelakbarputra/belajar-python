# 120; 12, 18
print("Selamat datang di Wahana Roller Coster")
tinggi = int(input("Berapa tinggimu? "))
bill = 0

if tinggi > 120:
    print("Kamu boleh naik rollercoster")
    umur = int(input("Kamu umur berapa? "))
    if umur < 12:
        bill = 5
        print(f"Anak kecil membayar ${bill}")
    elif umur <= 18: #18 < umur < 12
        bill = 7
        print(f"Remaja membayar ${bill}")
    else: # umur > 18
        bill = 12
        print(f"Dewasa membayar ${bill}")
    photo = input("Mau foto atau tidak Y or N? ")
    if photo == "Y":
        bill += 3
    print(f"Anda harus membayar sebesar ${bill}")
else:
    print("Kamu tidak boleh naik!")
print("Terima kasih! banyak")