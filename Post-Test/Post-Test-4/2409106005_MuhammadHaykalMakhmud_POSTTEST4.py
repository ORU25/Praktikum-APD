username = "haykal"
password = 5

for i in range(3):
    usernameInput = input("Masukkan username: ")
    passwordInput = int(input("Masukkan password: "))

    if usernameInput == username and passwordInput == password:
        print("Login Berhasil")
        while True:
            print("===================================")
            print("Kalkulator Kebutuhan Kalori Harian")
            print("===================================")
            print(" Masukkan Jenis Kelamin: ")
            print("1. Pria")
            print("2. Wanita")
            print("-----------------------------------")
    
            inputJenisKelamin = int(input())

            print("-----------------------------------------------")
            umur = int(input("Masukkan umur: "))
            print("-----------------------------------------------")
            print("-----------------------------------------------")
            beratBadanGram = float(input("Masukkan berat badan dalam satuan gram: "))
            beratBadanKG = beratBadanGram/1000
            print("-----------------------------------------------")
            print("-----------------------------------------------")
            tinggiBadanKM = float(input("Masukkan tinggi badan dalam satuan kilometer: "))
            tinggiBadanCM = tinggiBadanKM*100000
            print("-----------------------------------------------")
            print("-------------------------------------------------")
            print("Masukkan Level Aktivitas Harian: ")
            print("1. Aktivitas Minimal (jarang bergerak)")
            print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
            print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
            print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)")
            print("-------------------------------------------------")
            

            inputLevelAktivitas = int(input())

            invalidAktivitas = False

            if inputJenisKelamin == 1:
                BMR = 10*beratBadanKG + 6.25*tinggiBadanCM - 5*umur+5
                if inputLevelAktivitas == 1:
                    TDEE = BMR*1.25
                elif inputLevelAktivitas == 2:
                    TDEE = BMR*1.36
                elif inputLevelAktivitas == 3:
                    TDEE = BMR*1.72
                else:
                    invalidAktivitas = True

                if invalidAktivitas:
                    print("-----------------------------------------")
                    print("Harap pilih aktivitas harian yang benar")
                    print("-----------------------------------------")
                else:
                    print("------------------------------------------------------------")
                    print("Kebutuhan kalori harianmu sebanyak: "+ str(TDEE) + " kalori")
                    print("------------------------------------------------------------")
            elif inputJenisKelamin == 2:
                BMR = 10*beratBadanKG + 6.25*tinggiBadanCM - 5*umur-161
                if inputLevelAktivitas == 1:
                    TDEE = BMR*1.25
                elif inputLevelAktivitas == 2:
                    TDEE = BMR*1.36
                elif inputLevelAktivitas == 3:
                    TDEE = BMR*1.72
                else:
                    invalidAktivitas = True

                if invalidAktivitas:
                    print("-----------------------------------------")
                    print("Harap pilih aktivitas harian yang benar")
                    print("-----------------------------------------")
                else:
                    print("------------------------------------------------------------")
                    print("Kebutuhan kalori harianmu sebanyak: "+ str(TDEE) + " kalori")
                    print("------------------------------------------------------------")
            else:
                print("-----------------------------------------")
                print("Harap pilih jenis kelamin antara 1 atau 2")
                print("-----------------------------------------")

            ulang = input("Apakah ingin menghitung ulang ? (y/n) ")
            if ulang == "n" or ulang == "N":
                break
        break
    else:
        print("Username atau password yang anda masukkan salah")