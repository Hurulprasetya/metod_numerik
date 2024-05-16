def fungsi(x):
    # Ganti fungsi ini sesuai dengan fungsi yang ingin Anda tentukan
    return x**2 - 4

def turunan_fungsi(x):
    # Ganti turunan fungsi ini sesuai dengan turunan fungsi yang Anda tentukan
    return 2 * x

def newton_raphson(tebakan_awal, toleransi, maks_iterasi):
    iterasi = 0
    x = tebakan_awal

    while abs(fungsi(x)) > toleransi and iterasi < maks_iterasi:
        x = x - fungsi(x) / turunan_fungsi(x)
        iterasi += 1

    if abs(fungsi(x)) <= toleransi:
        return x, iterasi
    else:
        return None, iterasi

# Contoh penggunaan
tebakan_awal = float(input("Masukkan tebakan awal: "))
toleransi = float(input("Masukkan toleransi: "))
maks_iterasi = int(input("Masukkan jumlah maksimum iterasi: "))

hasil, iterasi = newton_raphson(tebakan_awal, toleransi, maks_iterasi)

if hasil is not None:
    print(f"Akar yang ditemukan: {hasil}")
    print(f"Jumlah iterasi: {iterasi}")
else:
    print("Metode Newton-Raphson tidak konvergen.")
