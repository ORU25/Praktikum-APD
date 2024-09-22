print("""===================================
Kalkulator Kebutuhan Kalori Harian
===================================
-----------------------------------
Masukkan Jenis Kelamin: 
1. Pria
2. Wanita
-----------------------------------""")

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
print("""-------------------------------------------------
Masukkan Level Aktivitas Harian: 
1. Aktivitas Minimal (jarang bergerak)
2. Aktivitas Sedang (olahraga 1-3 kali seminggu)
3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)
-------------------------------------------------""")

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