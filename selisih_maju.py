def fungsi(x):
    # Definisikan fungsi yang ingin diambil turunannya di sini
    return x**2

def turunan_selisih_maju(f, x, h):
    # Menghitung turunan menggunakan metode selisih maju
    return (f(x + h) - f(x)) / h

# input dari pengguna
x0 = float(input("Masukkan nilai x: "))
h = float(input("Masukkan nilai h (besaran langkah): "))

# Menghitung turunan menggunakan metode selisih maju
hasil_turunan = turunan_selisih_maju(fungsi, x0, h)

print(f'Turunan di {x0} dengan langkah {h} adalah: {hasil_turunan}')
