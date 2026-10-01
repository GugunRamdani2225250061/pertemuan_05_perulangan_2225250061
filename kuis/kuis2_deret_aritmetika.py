print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi banyak suku
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

# Inisialisasi total
total = 0

# Menghasilkan suku dan menghitung jumlah
for i in range(n):
    suku = a + i * d
    total += suku

    print(f"Suku ke-{i + 1}: {suku:.2f}")

# Menampilkan jumlah akhir
print(f"Jumlah deret: {total:.2f}")