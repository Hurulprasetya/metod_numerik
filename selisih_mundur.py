def fungsi(x):
    # Definisikan fungsi yang ingin diambil turunannya di sini
    return x**2

def turunan_selisih_mundur(f, x, h):
    # Menghitung turunan menggunakan metode selisih mundur
    return (f(x) - f(x - h)) / h

# input dari pengguna
x0 = float(input("Masukkan nilai x: "))
h = float(input("Masukkan nilai h (besaran langkah): "))

# Menghitung turunan menggunakan metode selisih mundur
hasil_turunan = turunan_selisih_mundur(fungsi, x0, h)

print(f'Turunan di {x0} dengan langkah {h} adalah: {hasil_turunan}')