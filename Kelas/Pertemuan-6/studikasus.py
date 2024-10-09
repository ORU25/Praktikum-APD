import os
os.system('cls')

# data = {
#     "Nama" : "Haykal",
#     "Umur": 18,
#     "NIM" : 2409106005,
#     "Jurusan": "Teknik Informatika",
#     "Angkatan": 2024
# }


# print(f"NIM = {data['NIM']}")

# data.update({"NIM": 2109106079})
# print(f"NIM = {data['NIM']}")


biodata = {}

while True:
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Exit")

    pilih = int(input("Pilih Menu: "))

    if pilih == 1:
        nama = input("Masukkan Nama: ")
        umur = int(input("Masukkan Umur: "))
        nim = int(input("Masukkan NIM: "))
        jurusan = input("Masukkan Jurusan: ")
        angkatan = int(input("Masukkan Angkatan: "))

        biodata[nama] = {"Umur": umur, "NIM": nim, "Jurusan": jurusan, "Angkatan": angkatan}

    elif pilih == 2:
        for nama, data in biodata.items():
            print(f"Nama: {nama}")
            print(f"Umur: {data['Umur']}")
            print(f"NIM: {data['NIM']}")
            print(f"Jurusan: {data['Jurusan']}")
            print(f"Angkatan: {data['Angkatan']}")
            print("")

    elif pilih == 3:
        break

    else:
        print("Pilihan Tidak Tersedia")