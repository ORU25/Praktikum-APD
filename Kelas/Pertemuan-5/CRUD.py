data_mahasiswa = []
print(
"""
========================
|   DATA MAHASISWA     |
========================
1. tambah data
2. lihat data
3. ubah data
4. hapus data
5. keluar
========================
"""
)

while True:
    pilihan = int(input("masukkan pilihan: "))
    if pilihan == 1:
        print("Tambah Data")
        nama = input("masukkan nama: ")
        nim = input("masukkan nim: ")
        kelas = input("masukkan kelas: ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilihan == 2:
        print("Lihat Data")
        for data in data_mahasiswa:
            # for i in range(len(data_mahasiswa)):
                print(f"\nData Mahasiswa ke-{data_mahasiswa.index(data)+1} \nNama: {data[0]} \nNim: {data[1]} \nKelas: {data[2]}")
    elif pilihan == 3:
        print("ubah data")
        nama_lama = input("masukkan nama lama: ")
        for data in range(len(data_mahasiswa)):
            if data_mahasiswa[data][0] == nama_lama:
                data_mahasiswa[data][0] = input("masukkan nama: ")
                data_mahasiswa[data][1] = input("masukkan nim: ")
                data_mahasiswa[data][2] = input("masukkan kelas: ")

    elif pilihan == 4:
        print("hapus data")
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilihan == 5:
        print("keluar")
        break
    else:
        print("pilihan tidak tersedia")