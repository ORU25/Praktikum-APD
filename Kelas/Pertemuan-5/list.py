# nama = ["celio","shandy","farrel","ghazali","vito","yuyun","adri","rizal","adi","ifnu"]

matkul = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]
# data = nama+matkul

# print("sebelumnya: " )
# print(nama)
# print("sesudah: ")

# # nama.append("afrizal")
# # nama.insert(2,"afrizal")
# # nama[4] = "fufufafa"
# # del nama[2]
# # nama.clear()
# # someone = nama.pop(2)


# # print(nama)
# # print(someone)

# # print(nama[0:3])
# # print(nama[1:9:2])

# # print(data)
# # print(data*3)

# print(nama)


nestedList = [
    "farel",
    "celio",
    [
        1,
        2,
        [
            "a",
            "b",
            "c",
            True,
            11,
            12
        ]
    ]
]

# print(nestedList[2][2][3])
# print(nestedList[2][2][::-1])


# for i in matkul:
#     print(i, end=" ")

angka = [[1,2,3],[4,5,6],[7,8,9]]
for i in angka:
    for j in i:
        print(j)