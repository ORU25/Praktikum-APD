listAccount = {
      #unique key : {'username','password','role'}
      "admin":{'username':'admin','password':'admin123','role':'admin'},
      "user":{'username':'user','password':'user123','role':'user'},
}

listKamar = {
      #unique key : {'nomor','status'}
      "101":{"nomor":"101","status":"tersedia"},
      "102":{"nomor":"102","status":"terpakai"},
      "104":{"nomor":"103","status":"tersedia"},
      "105":{"nomor":"104","status":"terpakai"},
      "106":{"nomor":"105","status":"tersedia"},
}

while True:
      print("""
==================================================
| SELAMAT DATANG DI SISTEM PEMESANAN KAMAR HOTEL |
==================================================
| Pilih menu :                                   |
| 1. Login                                       |
| 2. Keluar                                      |
==================================================""")
      pilihMenu = input("Masukkan pilihan anda: ")
      if pilihMenu == '1':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            akunDitemukan = False

            for account in listAccount.values():
                  if username == account["username"] and password == account["password"]:
                        akunDitemukan = True
                        # Login sebagai admin
                        if account['role'] == 'admin':
                              while True:
                                    print("\n================================")
                                    print("| Login Sebagai Admin          |")
                                    print("================================")
                                    print("| Pilih menu :                 |")
                                    print("| 1. Register User             |")
                                    print("| 2. Manage Kamar              |")
                                    print("| 3. logout                    |")
                                    print("================================")

                                    pilihMenu = input("Masukkan pilihan anda: ")

                                    # Register User
                                    if pilihMenu == '1':
                                          print("Register User")
                                          usernameUser = input("Masukkan username user: ")
                                          usernameDitemukan = False
                                          for account in listAccount.values():
                                                if usernameUser == account["username"]:
                                                      usernameDitemukan = True
                                                      print("Username sudah ada. Tidak bisa menginput username yang sama")
                                                      break

                                          if usernameDitemukan == False:
                                                passwordUser = input("Masukkan password user: ")  
                                                listAccount[usernameUser] = {'username':usernameUser,'password':passwordUser,'role':'user'}
                                                print("User Berhasil Diregisterasi")
                                                print(listAccount)    
                                    
                                    # Manage Kamar
                                    elif pilihMenu == '2':
                                          while True:
                                                print("\n================================")
                                                print("| Menu Manage Kamar            |")
                                                print("================================")
                                                print("| Pilih menu :                 |")
                                                print("| 1. Tambah Kamar              |")
                                                print("| 2. Lihat Kamar               |")
                                                print("| 3. Update Kamar              |")
                                                print("| 4. Hapus Kamar               |")
                                                print("| 5. Kembali                   |")
                                                print("================================")

                                                pilihMenu = input("Masukkan pilihan anda: ")

                                                # Tambah Kamar
                                                if pilihMenu == '1':
                                                      nomorkamar = input("Masukkan nomor kamar: ")
                                                      kamarDitemukan = False

                                                      for kamar in listKamar.values():
                                                            if kamar["nomor"] == nomorkamar:
                                                                  kamarDitemukan = True
                                                                  print("Kamar sudah ada. Tidak bisa menambahkan kamar yang sama")
                                                                  break
                                                      if kamarDitemukan == False:
                                                            statuskamar = input("Masukkan status kamar: ")
                                                            listKamar[nomorkamar] = ({"nomor":nomorkamar,"status":statuskamar})
                                                            print("Kamar Berhasil Ditambahkan")

                                                # Lihat Kamar
                                                elif pilihMenu == '2':
                                                      print("\n===============================")
                                                      print("| Kode Kamar   | Status Kamar |")
                                                      print("===============================")
                                                      for kamar in listKamar.values():
                                                            print(f"| {kamar["nomor"]:<12} | {kamar["status"]:<12} |")
                                                      print("===============================")
                                                
                                                # Update Kamar
                                                elif pilihMenu == '3':
                                                      print("\n===============================")
                                                      print("| Kode Kamar   | Status Kamar |")
                                                      print("===============================")
                                                      for kamar in listKamar.values():
                                                            print(f"| {kamar["nomor"]:<12} | {kamar["status"]:<12} |")
                                                      print("===============================")

                                                      kamarLama = input("Masukkan kode kamar yang ingin diubah: ")
                                                      kamarDitemukan = False
                                                      for kamar in listKamar.values():

                                                            if kamar["nomor"] == kamarLama:
                                                                  kamarDitemukan = True
                                                                  kodeSudahAda = False
                                                                  kodeBaru = input("Masukkan kode kamar baru / kamar lama jika tidak ingin diubah: ")
                                                                  
                                                                  if kodeBaru != kamarLama:
                                                                        for kode in listKamar.values():
                                                                              if kode["nomor"] == kodeBaru:
                                                                                    kodeSudahAda = True
                                                                                    print("Kode kamar sudah ada.")
                                                                                    break

                                                                  while kodeSudahAda == False:
                                                                        statusBaru = input("Masukkan status kamar baru (tersedia / terpakai): ")
                                                                        if statusBaru != 'terpakai' and statusBaru != 'tersedia':
                                                                              print("Status kamar harus 'terpakai' atau 'tersedia'")
                                                                        else:
                                                                              kamar["nomor"] = kodeBaru
                                                                              kamar["status"] = statusBaru
                                                                              print("Kamar Berhasil Diubah")
                                                                              break
                                                                  break

                                                      if kamarDitemukan == False:
                                                            print("Kamar tidak ditemukan")     
                                                                  
                                                # Hapus Kamar
                                                elif pilihMenu == '4':
                                                      nomorkamar = input("Masukkan nomor kamar: ")

                                                      kamarDitemukan = False
                                                      for kamar in listKamar.values():
                                                            if kamar["nomor"] == nomorkamar:
                                                                  kamarDitemukan = True
                                                                  del listKamar[nomorkamar]
                                                                  print("Kamar Berhasil Dihapus")
                                                                  break
                                                      
                                                      if kamarDitemukan == False:
                                                            print("Kamar tidak ditemukan")

                                                elif pilihMenu == '5':
                                                      break
                                                else:
                                                      print("Pilihan yang anda masukkan salah")
                                    elif pilihMenu == '3':
                                          break
                                    else:
                                          print("Pilihan yang anda masukkan salah")
                              break
                        # Login Sebagai User
                        elif account['role'] == 'user':
                              while True:
                                    print("\n================================")
                                    print("| Login Sebagai User           |")
                                    print("================================")
                                    print("| Pilih menu :                 |")
                                    print("| 1. pesan Kamar               |")
                                    print("| 2. logout                    |")
                                    print("================================")

                                    pilihMenu = input("Masukkan pilihan anda: ")
                                    
                                    # Pesan Kamar
                                    if pilihMenu == '1':  
                                          kamarTersedia = False

                                          print("\n================================")
                                          print("| List Kamar Tersedia         |")
                                          print("===============================")
                                          print("| Kode Kamar   | Status Kamar |")
                                          print("===============================")
                                          for kamar in listKamar.values():
                                                if kamar["status"] == 'tersedia':
                                                      kamarTersedia = True
                                                      print(f"| {kamar["nomor"]:<12} | {kamar["status"]:<12} |")
                                          if kamarTersedia == False:
                                                print("| Tidak ada kamar tersedia    |")
                                          print("===============================")

                                          if kamarTersedia == True:
                                                nomorkamar = input("Masukkan nomor kamar yang ingin anda pesan: ")
                                                kamarDitemukan = False
                                                for kamar in listKamar.values():
                                                      if kamar["nomor"] == nomorkamar:
                                                            kamarDitemukan = True
                                                            if kamar["status"] == 'tersedia':
                                                                  kamar["status"] = 'terpakai'
                                                                  print("Kamar Berhasil Diambil")
                                                                  break
                                                            else:
                                                                  print("Kamar tersebut sedang terpakai")
                                                if kamarDitemukan == False:
                                                      print("Kamar tidak ditemukan")
                                    

                                    elif pilihMenu == '2':
                                          break
                                    else:
                                          print("Pilihan yang anda masukkan salah")
                              
            if akunDitemukan == False:
                  print("Username atau password yang anda masukkan salah")
                  

      elif pilihMenu == '2':
            break
      else:
            print("Pilihan yang anda masukkan salah")