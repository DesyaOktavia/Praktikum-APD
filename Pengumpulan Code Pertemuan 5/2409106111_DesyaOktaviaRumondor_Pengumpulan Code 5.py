# LIST
# nama = ["desya", 106, True, 3.96]
# matkul = ["APD","APL","WEB","JARKOM"]
# print(nama)
# print(matkul)

# kalau pemogram ingin mengeprint beberapa elemen saja
# print(nama[1])
# print(matkul[2])
# print(matkul[-1])
# print(matkul[-2])
# print(matkul[-3])


# nama = ["desya", 106, True, 3.96, [123,"DESYA",False,3.66],"rehan"]
# print(nama[4][2])
# print(nama[4][3])

# nama = ["desya", 106, True,["yuyun",145] 3.96, [123,"DESYA",False,3.66],"rehan"]
# print(nama[5][0])
# print(nama[4])


# matkul = ["APD",
#           "APL",
#           "WEB",
#           "JARKOM",
#           "BASDAT",
#           "STRUKDAT",
#           "PTI",
#           "KALKULUS",
#           "PROBAS"
# ]
# print(matkul[-3])
# print(matkul[6])


# MENAMBAHKAN DIAKHIR
# makanan = ["Bakso","Sate","Soto"]
# print("Sebelum: ")
# print(makanan)
# makanan.append("Nasi Goreng")
# print("Sesudah: ")
# print(makanan)

# MENAMBAHKAN DITENGAH
# makanan = ["Bakso","Sate","Soto"]
# print("Sebelum: ")
# print(makanan)
# print("Sesudah: ")
# makanan.insert(1,"Nasi Goreng")
# print(makanan)
# makanan.insert(0,"Nasi Goreng")
# print(makanan)
# makanan.insert(2,"Nasi Goreng")
# print(makanan)

# MENGUBAH
# makanan = ["Bakso","Sate","Soto"]
# makanan[1] = "Nasi Goreng"
# print(makanan)
# makanan[0] = "123"
# print(makanan)
# makanan[2] = ["AYAM","BEBEK"]
# print(makanan)

# makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Ayam","Ayam bakar","Cumi Goreng"]
# print("Sebelum: ")
# print(makanan [2:5])
# print("Sesudah: ")
# print(makanan)

# MENGHAPUS
# makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Ayam","Ayam bakar","Cumi Goreng"]
# print("Sebelum: ")
# print(makanan)
# del makanan [2]
# print("Sesudah: ")
# print(makanan)

# makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Ayam","Ayam bakar","Cumi Goreng"]
# print("Sebelum: ")
# print(makanan)
# del makanan [0:2]
# print("Sesudah: ")
# print(makanan)

# makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Ayam","Ayam bakar","Cumi Goreng"]
# print("Sebelum: ")
# print(makanan)
# del makanan [2: ]
# print("Sesudah: ")
# print(makanan)

# makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Ayam","Ayam bakar","Cumi Goreng"]
# print("Sebelum: ")
# print(makanan)
# data = makanan.pop(1)
# print("Sesudah: ")
# print(makanan)
# print (data)

# makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Ayam","Ayam bakar","Cumi Goreng"]
# print("Sebelum: ")
# makanan.clear()
# print("Sesudah: ")
# print(makanan)


# soal latihan: +
# ada minuman 6. elemen 3(dihapus), elemen 6(diganti air putih), elemen 0(ditambahkan jus tomat)

# minuman = ["Pucuk","Jus Buah","Es Buah","Es Teh","Bintang","Orang Tua"]

# print("Sebelum: ")
# print(minuman)
# del minuman [2]
# print("Sesudah: ")
# print(minuman)
# minuman[4] = "Air Putih"
# print("Sesudah: ")
# print(minuman)
# minuman.insert(0,"Jus tomat")
# print("Sesudah: ")
# print(minuman)



# Perulangan for
# makanan = ["Bakso","Soto","Sate"]
# for i in makanan :
#     print(i)

# makanan = ["Bakso","Soto","Sate","Ikan","Bebek"]
# for i in makanan :
#     print(i)

# makanan = ["Bakso","Soto","Sate","Ikan","Bebek"]
# for i in makanan :
#     print(i, end=" ")

# makanan = ["Bakso","Soto","Sate","Ikan","Bebek"]
# for i in makanan :
#     print(i, end="&")



# PERULANGAN NESTED MENGGUNAKAN for
# makanan = [["Bakso","Soto","Sate","Ikan","Bebek"],["Teh","Kopi","Air"]]

# for i in makanan :
#     for j in i :
#         print(j, end=" ")

# makanan = ["Ayam","Ikan",["Bakso","Soto","Sate","Ikan","Bebek"],["Teh","Kopi","Air"]]

# for i in makanan :
#     if isinstance(i, list) :
#         for j in i :
#             print(j)
#     else :
#         print(i)



# TUPLE
# nama = ("rizky", "abdullah", "reza")
# print (nama[0])
# print (nama[1])
# print (nama[2])


# CSV atau CSP
# CRUD


akuns = []

while True :
    print("Halo Selamat Datang Di Aplikasi Catatan")
    print("Silahkan Pilih 'Daftar Akun' Jika Belum Buat Akun, dan Jika Sudah Memiliki Akun Silahkan 'Login'")
    print("1, Daftar Akun")
    print("2, Login")
    print("3, Exit")
    print("_________________________")
    opsi = input("Pilih opsi: ")
    print(" ")
    
    if opsi == "1" :
        print("Halo Pengguna Baru! Ayo Buat Akun Dulu")
        username = input("username: ")
        akuna = False
        for akun in akuns :
            if akun[0] == username: #memeriksa apakah username sudah ada
                akuna == True
                break
        if akuna :
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else :
            Password = input("Password: ")
            akuns.append([username, Password, []]) #Simpan Username, Password, dan Catatan (Sebagai list kosong)
            print(f"akun Anda Berhasil Terdaftar Dengan ID: {username}")