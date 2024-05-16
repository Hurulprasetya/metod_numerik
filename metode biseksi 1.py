def fungsi(x):
    # Ganti fungsi ini sesuai dengan fungsi yang ingin Anda tentukan
    return 2 * x**2 + 3 * x - 4

def metode_biseksi(a, b, toleransi):
    if fungsi(a) * fungsi(b) > 0:
        print("Perhatian: Metode biseksi dijalankan meskipun f(a) * f(b) > 0. Hasil mungkin tidak akurat.")

    iterasi = 0
    while (b - a) / 2 > toleransi:
        c = (a + b) / 2
        if fungsi(c) == 0:
            return c, iterasi  # Akar ditemukan tepat
        elif fungsi(c) * fungsi(a) < 0:
            b = c
        else:
            a = c
        iterasi += 1

    return (a + b) / 2, iterasi

# Masukkan nilai awal a, b, dan toleransi
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
toleransi = float(input("Masukkan toleransi: "))

# Panggil metode_biseksi dan cetak hasilnya
hasil, iterasi = metode_biseksi(a, b, toleransi)

print(f"Akar yang ditemukan: {hasil}")
print(f"Jumlah iterasi: {iterasi}")
