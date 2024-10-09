import os
os.system('cls')

# buku = {
#     "BUku1" : "Harry Potter",
#     "BUku2" : "Percy Jackson",
#     "BUku3" : "Twilight",
# }

# print(buku["BUku1"])
# print(buku)

Biodata = {
    "Nama" : "Aldy Ramadhan Syahputra",
    "NIM" : 2109106079,
    "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" :True,
    "Social Media" : {
        "Instagram" : "@aldyrmdhns_",
        "Discord" : "\'Izanami#6848"
    }
}

# print(Biodata["krs"][0])
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat", "Tidak ada"))
# print(Biodata["Social Media"]["Discord"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = "FPS")
# print(games)

# for i, j in Biodata.items():
#     print(i, ":", j)

Film = {
    "Avenger Endgame" : "Action",
    "Sherlock Holmes" : "Mystery",
    "The Conjuring" : "Horror"
}

# Film["Thomas"] = "Comedy"
# Film.update({"Hourly":"Horror"})

# del Film["Avenger Endgame"]

# hapus = Film.pop("The Conjuring")
# print(f"{hapus} telah di hapus")

# Film.clear()
# print(Film)


# print(len(Biodata))

# copyan = Biodata.copy()
# print(copyan)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# for i in Film.values():
#     print(i, end=' ')

# print(Film)
# print(Film.setdefault("OldBook", "Horror"))
# print(Film)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)
# del mahasiswa[111]["Umur"]
# print(mahasiswa)