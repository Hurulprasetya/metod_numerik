from sympy import sympify, symbols
import numpy as np
import matplotlib.pyplot as plt

# Meminta pengguna untuk memasukkan persamaan fungsi matematika.
fungsi1 = input("Persamaan fungsi: ")

# Meminta pengguna untuk memasukkan nilai A, B, dan jumlah iterasi.
nilaia = float(input("Nilai A: "))
nilaib = float(input("Nilai B: "))
iterasi = int(input("Iterasi: "))

# Membuat simbol matematika untuk x.
variabel_x = symbols("x")

# Mengubah persamaan fungsi yang dimasukkan oleh pengguna menjadi format yang dapat dihitung oleh SymPy.
fungsi_perhitungan = sympify(fungsi1)

# Fungsi untuk mengartikan nilai input menjadi nilai fungsi pada suatu titik x.
def fungsi(nilai):
    c = fungsi_perhitungan.subs(variabel_x, nilai).evalf()
    return c

# Fungsi dummy yang akan digunakan untuk plotting.
def fungsi2(nilai2):
    return nilai2

# Implementasi metode biseksi untuk mencari akar persamaan.
def biseksi(nilaia, nilaib, tot):
    # Inisialisasi variabel.
    n = 1
    x = nilaia  # Memberikan nilai awal ke x di luar loop

    # Memeriksa apakah interval [A, B] mengandung akar persamaan.
    if fungsi(nilaia) * fungsi(nilaib) > 0:
        print("Tidak memiliki akar persamaan")
    else:
        # Menampilkan pesan jika interval [A, B] memiliki akar persamaan.
        print("Akar persamaan {} dan {}".format(nilaia, nilaib))
        # Menampilkan header tabel penolong.
        print("{:<5} {:<12} {:<12} {:<12} {:<20} {:<20} {}".format("n", "a", "b", "xn", "f(a)", "f(b)", "f(xn)"))

        # Melakukan iterasi sampai selisih (B - A) / 2 kurang dari toleransi yang diinginkan.
        while (nilaib - nilaia) / 2 > tot:
            # Menampilkan informasi setiap iterasi.
            print("Iterasi ke-{}: nilaia = {}, nilaib = {}, (nilaib - nilaia) / 2 = {}".format(n, nilaia, nilaib, (nilaib - nilaia) / 2))
            # Menghitung nilai fungsi pada titik A, B, dan tengah (x).
            fungsi_nilai_a = fungsi(nilaia)
            fungsi_nilai_b = fungsi(nilaib)
            x = (nilaia + nilaib) / 2
            fungsi_nilai_n = fungsi(x)
            # Menampilkan nilai-nilai pada tabel penolong.
            print("{:<5} {:<12f} {:<12f} {:<12f} {:<20f} {:<20f} {}".format(n, nilaia, nilaib, x, fungsi_nilai_a, fungsi_nilai_b, fungsi_nilai_n))

            # Mengecek apakah nilai fungsi pada titik tengah (x) adalah akar persamaan.
            if fungsi(x) == 0:
                return x
            # Menentukan interval berikutnya.
            elif fungsi(nilaia) * fungsi(x) < 0:
                nilaib = x
            else:
                nilaia = x
            # Menaikkan counter iterasi.
            n += 1
        # Mengembalikan nilai akar yang ditemukan.
        return x

# Memanggil fungsi biseksi dan menampilkan akar yang ditemukan.
jawaban = biseksi(nilaia, nilaib, iterasi)
print("Akar Persamaannya adalah ", round(jawaban, 5))

# Membuat plot grafik fungsi pada interval [A, B].
x = np.linspace(nilaia, nilaib, 100)
plt.plot(x, fungsi2(x))
plt.grid()
plt.show()