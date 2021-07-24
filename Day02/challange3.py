# asumsi umur maks adalah 90 dan 365 hari, 52 minggu, 12 bulan
# semua yang dimasukkan ke input bertipe string, jd harus dikonversi dulu
# semua yang dioperasikan dengan float akan menjadi float
age = int(input("Berapa umurmu sekarang? "))

current_month = (90 - age) * 12
current_week = (90 - age) * 52
current_day = (90 - age) * 365

print(f"You have {current_day} days left, {current_week} weeks left, and {current_month} month left")
