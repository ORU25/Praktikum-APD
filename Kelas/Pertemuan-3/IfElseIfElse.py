print("=== MENU ===")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
pilih = int(input("Pilih: "))

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if pilih == 1:
    print(angka1 + angka2)
elif pilih == 2:
    print(angka1 - angka2)
elif pilih == 3:
    print(angka1 * angka2)
elif pilih == 4:
    print(angka1 / angka2)
else:
    print("Pilihan tidak tersedia")