jumlah = int(input("Jumlah mahasiswa : "))

while jumlah < 5 or jumlah > 10:
    print("Jumlah harus antara 5 sampai 10!")
    jumlah = int(input("Jumlah mahasiswa (5-10): "))

total = 0

for i in range(1, jumlah + 1):
    nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
    total += nilai

rata_rata = total / jumlah
print(f"Nilai rata - rata : {rata_rata}")