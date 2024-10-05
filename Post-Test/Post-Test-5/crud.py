listAccount = [
      ['admin','admin123'],
      ['user','user123'],
]


listKamar = [
      ['101','tersedia'],
      ['102','terpakai'],
      ['103','tersedia'],
      ['104','terpakai'],
      ['105','tersedia']
]


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
            for i in range(len(listAccount)):
                  # Login admin
                  if username == listAccount[0][0] and password == listAccount[0][1]:
                        akunDitemukan = True
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
                                    passwordUser = input("Masukkan password user: ")

                                    listAccount.append([usernameUser, passwordUser])
                                    
                                    print("User Berhasil Diregisterasi")
                              
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
                                                statuskamar = input("Masukkan status kamar: ")

                                                listKamar.append([nomorkamar,statuskamar])

                                                print("Kamar Berhasil Ditambahkan")

                                          # Lihat Kamar
                                          elif pilihMenu == '2':
                                                print("\n===============================")
                                                print("| Kode Kamar   | Status Kamar |")
                                                print("===============================")
                                                for kamar in listKamar:
                                                      print(f"| {kamar[0]:<12} | {kamar[1]:<12} |")
                                                print("===============================")
                                          
                                          # Update Kamar
                                          elif pilihMenu == '3':
                                                print("\n===============================")
                                                print("| Kode Kamar   | Status Kamar |")
                                                print("===============================")
                                                for kamar in listKamar:
                                                      print(f"| {kamar[0]:<12} | {kamar[1]:<12} |")
                                                print("===============================")

                                                kamarLama = input("Masukkan kode kamar yang ingin diubah: ")
                                                for kamar in range(len(listKamar)):
                                                      kamarDitemukan = False

                                                      if listKamar[kamar][0] == kamarLama:
                                                            kamarDitemukan = True
                                                            kodeSudahAda = False
                                                            kodeBaru = input("Masukkan kode kamar baru: ")
                                                            for kode in listKamar:
                                                                  if kode[0] == kodeBaru:
                                                                        kodeSudahAda = True
                                                                        print("Kode kamar sudah ada. Tidak bisa mengubah ke kode yang sama.")
                                                                  break
                                                            if kodeSudahAda == False:
                                                                  statusBaru = input("Masukkan status kamar baru: ")
                                                                  listKamar[kamar][0] = kodeBaru
                                                                  listKamar[kamar][1] = statusBaru
                                                                  print("Kamar Berhasil Diubah")
                                                      break
                                                if kamarDitemukan == False:
                                                      print("Kamar tidak ditemukan")     
                                                            
                                          # Hapus Kamar
                                          elif pilihMenu == '4':
                                                nomorkamar = input("Masukkan nomor kamar: ")

                                                kamarDitemukan = False
                                                for kamar in range(len(listKamar)):
                                                      if listKamar[kamar][0] == nomorkamar:
                                                            kamarDitemukan = True
                                                            listKamar.remove(listKamar[kamar])
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
                  

                  # Login User
                  elif username == listAccount[i][0] and password == listAccount[i][1]:
                        akunDitemukan = True
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
                                    print("\n================================")
                                    print("| List Kamar Tersedia         |")
                                    print("===============================")
                                    print("| Kode Kamar   | Status Kamar |")
                                    print("===============================")
                                    for kamar in listKamar:
                                          if kamar[1] == 'tersedia':
                                                print(f"| {kamar[0]:<12} | {kamar[1]:<12} |")
                                    print("===============================")

                                    nomorkamar = input("Masukkan nomor kamar yang ingin anda pesan: ")
                                    kamarDitemukan = False
                                    for kamar in range(len(listKamar)):
                                          if listKamar[kamar][0] == nomorkamar:
                                                kamarDitemukan = True
                                                if listKamar[kamar][1] == 'tersedia':
                                                      listKamar[kamar][1] = 'terpakai'
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