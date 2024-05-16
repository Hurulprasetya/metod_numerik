def fungsi(x):
    # Definisikan fungsi yang ingin diambil turunannya di sini
    return x**2

def turunan_selisih_pusat(f, x, h):
    # Menghitung turunan menggunakan metode selisih pusat
    return (f(x + h) - f(x - h)) / 2*h

# input dari pengguna
x0 = float(input("Masukkan nilai x: "))
h = float(input("Masukkan nilai h (besaran langkah): "))

hasil_turunan = turunan_selisih_pusat(fungsi, x0, h)

print(f'Turunan di {x0} dengan langkah {h} adalah: {hasil_turunan}')