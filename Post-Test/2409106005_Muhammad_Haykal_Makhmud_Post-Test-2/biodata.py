NamaLengkap = input("Masukkan Nama Lengkap: ")
NamaPanggilan = input("Masukkan Nama Panggilan: ")
NIM = int(input("Masukkan NIM: "))
Prodi = input("Masukkan Program Studi: ")
Umur = int(input("Masukkan Umur: "))
TinggiBadan = float(input("Masukkan Tinggi Badan (Meter) contoh: 1.75: "))

tigaDigitTerakhirNIM = NIM % 1000
ModulusNIM = tigaDigitTerakhirNIM % 6

print("Perkenalkan nama saya " + NamaLengkap + ", biasa dipanggil " + NamaPanggilan + ", NIM saya " + str(NIM))
print("Program Studi saya " + Prodi + ", umur saya " + str(Umur) + " tahun, tinggi badan saya " + str(TinggiBadan) + " meter")
print("dan hasil modulus 6 dari 3 angka terakhir NIM saya adalah " + str(ModulusNIM))