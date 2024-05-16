from sympy import sympify, symbols
import numpy as np
import matplotlib.pyplot as plt

# 1. Masukkan persamaan fungsi x
fungsi1 = input("Persamaan fungsi: ")
nilaia = float(input("Nilai A: "))
nilaib = float(input("Nilai B: "))
iterasi = int(input("Iterasi: "))

variabel_x = symbols("x")
fungsi_perhitungan = sympify(fungsi1)

# 2. Buat fungsi untuk mengartikan input ke fungsi
def fungsi(nilai):
    c = fungsi_perhitungan.subs(variabel_x, nilai)
    return c

def fungsi2(nilai2):
    return nilai2

# 3. Buat fungsi biseksi
def biseksi(nilaia, nilaib, tot):
    n = 1
    x = nilaia  # Memberikan nilai awal ke x di luar loop
    if fungsi(nilaia) * fungsi(nilaib) > 0:
        print("Tidak memiliki akar persamaan")
    else:
        print("Akar persamaan {} dan {}".format(nilaia, nilaib))
        print("%-5s %-10s %-10s %-10s %-12s %-10s %s" % ("n", "a", "b", "xn", "f(a)", "f(b)", "f(xn)"))
        while (nilaib - nilaia) / 2 > tot:
            fungsi_nilai_a = fungsi(nilaia)
            fungsi_nilai_b = fungsi(nilaib)
            x = (nilaia + nilaib) / 2
            fungsi_nilai_n = fungsi(x)
            print("%-5d %-10f %-10f %-10f %-10f %-10f %f" % (n, nilaia, nilaib, x, fungsi_nilai_a, fungsi_nilai_b, fungsi_nilai_n))
            if fungsi(x) == 0:
                return x
            elif fungsi(nilaia) * fungsi(x) < 0:
                nilaib = x
            else:
                nilaia = x
            n += 1
        return x

# 4. Panggil fungsi biseksi dan tampilkan tabel penolongnya
jawaban = biseksi(nilaia, nilaib, iterasi)
print("Akar Persamaannya adalah ", round(jawaban, 5))

# 5. Buat plot grafik fungsi
x = np.linspace(nilaia, nilaib, 100)
plt.plot(x, fungsi2(x))
plt.grid()
plt.show()
