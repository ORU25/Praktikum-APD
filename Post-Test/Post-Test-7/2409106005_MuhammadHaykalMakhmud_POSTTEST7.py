listAccount = [
    # {'username','password','role'}
    {'username':'admin','password':'admin123','role':'admin'},
    {'username':'user','password':'user123','role':'user'},
]

listKamar = [
    #{'nomor','status'}
    {"nomor":"101","status":"tersedia"},
    {"nomor":"102","status":"terpakai"},
    {"nomor":"103","status":"tersedia"},
    {"nomor":"104","status":"terpakai"},
    {"nomor":"105","status":"tersedia"},
]

def login(username,password):
    for account in listAccount:
        result =""
        if username == account["username"] and password == account["password"]:
            if account["role"] == "admin":
                result = "admin"
            elif account["role"] == "user":
                result = "user"
            return result
    return result

def register(username,password):
    result = ""
    for account in listAccount:
        if username == account["username"]:
            result = "Username sudah ada"
            return result
    listAccount.append({'username':username,'password':password,'role':'user'})
    result = "success"
    return result

def bikinMenu(judul, pilihan):
    print("=" * 50)
    print(f"| {judul.center(46)} |")
    print("=" * 50)
    print("| Pilih menu :".ljust(49) + "|")
    
    for nomor, item in enumerate(pilihan, start=1):
        print(f"| {nomor}. {item.ljust(43)} |")

    print("=" * 50)

def createKamar():
    nomorkamar = input("Masukkan nomor kamar: ")
    kamarDitemukan = False

    for kamar in listKamar:
        if kamar["nomor"] == nomorkamar:
                kamarDitemukan = True
                print("Kamar sudah ada. Tidak bisa menambahkan kamar yang sama")
                break
    if kamarDitemukan == False:
        statuskamar = input("Masukkan status kamar (terpakai/tersedia): ")
        if statuskamar == 'tersedia' or statuskamar == 'terpakai':
            listKamar.append({"nomor":nomorkamar,"status":statuskamar})
            print("Kamar Berhasil Ditambahkan")
        else:
            print("Status kamar tidak valid")

def readKamar():
    print("\n===============================")
    print("| Kode Kamar   | Status Kamar |")
    print("===============================")
    for kamar in listKamar:
        print(f"| {kamar['nomor']:<12} | {kamar['status']:<12} |")
    print("===============================")

def cariKamar(listKamar, nomorKamar, index=0):
    if index == len(listKamar):
        return None    
    if listKamar[index]["nomor"] == nomorKamar:
        return listKamar[index]
    return cariKamar(listKamar, nomorKamar, index + 1)

def updateKamar(nomorKamar):
    kamar = cariKamar(listKamar, nomorKamar)
    if kamar:
        kodeBaru = input("Masukkan kode kamar baru / kamar lama jika tidak ingin diubah: ")
        if kodeBaru != nomorKamar and cariKamar(listKamar, kodeBaru) is None:
            kamar["nomor"] = kodeBaru
        statusBaru = input("Masukkan status kamar baru (tersedia / terpakai): ")
        if statusBaru in ['tersedia', 'terpakai']:
            kamar["status"] = statusBaru
            print("Kamar Berhasil Diubah")
        else:
            print("Status kamar tidak valid")
    else:
        print("Kamar tidak ditemukan")  

def deleteKamar(nomorKamar):
    kamarDitemukan = False
    for kamar in listKamar:
        if kamar["nomor"] == nomorKamar:
            kamarDitemukan = True
            listKamar.remove(kamar)
            print("Kamar Berhasil Dihapus")
            break
    
    if kamarDitemukan == False:
        print("Kamar tidak ditemukan")

def pesanKamar():
    judulMenu = "List Kamar Tersedia"
    pilihanMenu = []
    for kamar in listKamar:
        if kamar["status"] == "tersedia":
            pilihanMenu.append(kamar["nomor"])
    bikinMenu(judulMenu,pilihanMenu)

    nomorkamar = input("Masukkan nomor kamar: ")
    kamarDitemukan = False
    for kamar in listKamar:
        if kamar["nomor"] == nomorkamar:
            kamarDitemukan = True
            if kamar["status"] == "tersedia":
                kamar["status"] = "terpakai"
                print("Kamar Berhasil Dipesan")
                break
            else:
                print("Kamar tersebut sedang terpakai")
    if kamarDitemukan == False:
        print("Kamar tidak ditemukan")


def main():
    while True:
        bikinMenu("SELAMAT DATANG DI SISTEM PEMESANAN KAMAR HOTEL", ["Login","Keluar"])
        
        pilihMenu = input("Masukkan pilihan anda: ")
        if pilihMenu == '1':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if login(username,password) == "admin":
                while True:
                    bikinMenu("SELAMAT DATANG ADMIN", ["Register User","Manage Kamar","Logout"])

                    pilihMenuAdmin = input("Masukkan pilihan anda: ")

                    if pilihMenuAdmin == '1':
                        usernameUser = input("Masukkan Username: ")
                        passwordUser = input("Masukkan Password: ")

                        result = register(usernameUser,passwordUser)
                        
                        if result == "success":
                            print("User Berhasil Diregisterasi")
                        else:
                            print(result)


                    elif pilihMenuAdmin == '2':
                        while True:
                            bikinMenu("MANAGE KAMAR", ["Tambah Kamar","Lihat Kamar","Ubah Kamar","Hapus Kamar","Kembali"])

                            pilihMenuAdmin = input("Masukkan pilihan anda: ")
                            if pilihMenuAdmin == '1':
                                createKamar()
                            elif pilihMenuAdmin == '2':
                                readKamar()
                            elif pilihMenuAdmin == '3':
                                readKamar()
                                nomorKamar = input("Masukkan nomor kamar: ")
                                updateKamar(nomorKamar)
                            elif pilihMenuAdmin == '4':
                                readKamar()
                                nomorKamar = input("Masukkan nomor kamar: ")
                                deleteKamar(nomorKamar)
                            elif pilihMenuAdmin == '5':
                                break
                            else:
                                print("Pilihan yang anda masukkan salah")
                    elif pilihMenuAdmin == '3':
                        break
                    else:
                        print("Pilihan yang anda masukkan salah")
            elif login(username,password) == "user":
                while True:
                    bikinMenu("SELAMAT DATANG USER", ["Pesan Kamar","Logout"])

                    pilihMenuUser = input("Masukkan pilihan anda: ")
                    if pilihMenuUser == '1':
                        pesanKamar()
                    elif pilihMenuUser == '2':
                        break
                    else:
                        print("Pilihan yang anda masukkan salah")
            else:
                print("Username atau password yang anda masukkan salah")

        elif pilihMenu == '2':
            break
        else:
            print("Pilihan yang anda masukkan salah")


if __name__ == "__main__":
    main()