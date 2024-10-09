#Dictionary

#Deklarasi
# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# # print(daftar_buku["Buku2"])
# # print(daftar_buku["Buku3"])

# # print(daftar_buku)


# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku1" : "Twillight"
# }

# print(daftar_buku["Buku1"]) #data akan terupdate sendiri karena keyword buku1 ada 2 dan yang muncul yang paling baru



#cara biasa deklarasi of list menggunakan dictionary
# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848",
# "Email" : "iniemail@gmail.com"
#     }
# }

# print(Biodata["KRS"][0])
# print(Biodata["KRS"][0:])
# print(Biodata["Nama panggilan"]) #error
# print(Biodata["Social Media"]) 
# print(Biodata["Social Media"]["Discord"])
# print(Biodata["Social Media"]["Email"]) #print list variabel sesuai data index angka [], tetapi index variabel{}



#cara lain deklarasi menggunakan dict()
# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")

# print(games)
# print(games["Pokemon"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "Informatika"}})

# print(games['Valorant'['nama'][123]])


#Pengingat : disarankan print key dict menggunakan tanda petik satu, jika 2 biasanya akan error


#perbandingan dari cara deklarasi 1 dan deklarasi 2
#Cara 1
# Games ={
#     "Game1" : "PUBG MOBILE",
# }
#Cara 2
# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")


#Penggunaan get
# Games ={
#     "Game1" : "PUBG MOBILE",
#     "Game2" : "Mobile Legend",
#     "Game3" : "COC",
# }

# print(Games.get('Game3'))


# Games ={
#     "Game1" : "PUBG MOBILE",
#     "Game2" : "Mobile Legend",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" : "Strategy"
#     },
# }

# print((Games.get('Game3')).get('genre'))



#Dictionary dengan perulangan
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

#tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")

#menggunakan items
# for i, j in Nilai.items():   #Variabel i dan j itu bebas bisa diganti sesuai data yang tertera
#     print(f"Nilai {i} anda adalah {j}")   #Cara ini bisa digunakkan dalam Read Posttest



#Fitur Create untuk Dictionary
# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# #Create
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hour" : "Comedy", "Oblivion" : "Science Fiction"})
# #Setelah Ditambah
# print(Film)

# #Cara Create dan Update itu kurang lebih

# #Fitur Update Pada Dictionary
# Film["The Conjuring"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)


#Fitur Update pada dictionary
# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# #Sebelum Diubah
# print(Film)


# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})

# #Setelah diubah
# print(Film)


#Fitur Delete pada Dictionary

#Menggunakan Del
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }

# #Sebelum Dihapus
# print(data)
# del data["Nama"]

# #Setelah diubah
# print(data)

# #memanggil data yang telah dihapus
# print(data.get("Nama"))

#Menggunakkan pop
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

#Menggunakan Clear
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# data.clear()
# #Setelah dihapus
# print(data)


#Len dalam Dictionary
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))


#Copy dalam Dictionary
# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)


#Fromkeys dalam Dictinary #cocok nya hanya mengeprint value nya 1
# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)


#Contoh
# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# Film["Sherlock Holmes"] = "Action"
# Film.update({"Hours" : "Thriller",
#              "Rush Hours" : "Comedy",
#              "Oblivion" : "Science Fiction"})

# #Menggunakan Del  #Menghapus variabel key 
# del Film['Avenger Endgame']

# #Menggunakan Pop 
# print(Film)
# simpan = Film.pop('Hours')

# #Menggunakan Clear
# print(Film)
# Film ['Hours'] = simpan
# print(Film)

# #menggunkan len
# print("Jumlah Film = ", len(Film))

#Menggunakkan Copy
# movies = Film.copy()
# print(movies)
# print("Jumlah Film = ", len(Film))

#Menggunakkan From keys




#Menggunakkan Setdefaults
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
# print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
# print(i)

# #Sebelum Setdefaults
# print(Nilai)
# print(" ")

# #Menggunakkan Setdefaults
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print(" ")

# #Setelah menggunakkan Setdefaults
# print(Nilai)


#Dictionary of List 
# Musik = {
# "The Chainsmoker" : ["All we Know",  "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")


#Nested Dictionary
# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key) #key: 101 dan 111   #value menampilkan semua nya dari kurung siku
#     for key_a, value_a in value.items(): #key a: nama dan umur  #value a:  aldy 19, abdul 18
#         print (key_a, " : ", value_a)
# print("")





#Latihan Soal
print("===========================================================================================")
Biodata = {
    "Nama" : "Desya Oktavia Rumondor", 
    "Umur" : 18, 
    "NIM" : 2409106111, 
    "Jurusan" : "Informatika", 
    "Fakultas" : "Teknik"
}
print(Biodata)
print("===========================================================================================")
print(" ")

#Menambahkan Item baru sesuai dengan inputan User
print("===========================================================================================")
print("Menambahkan data")
Biodata["Angkatan"] = 24
print(Biodata)
print("===========================================================================================")
print(" ")

# Mengubah salah satu key sesuai dengan inputan User
print("===========================================================================================")
print("Mengubah data")
Biodata["Umur"] = 19
Biodata.update({"Umur" : 19})
print(Biodata)
print("===========================================================================================")
print(" ")

#Menghapus salah satu key sesuai dengan Inputan user
print("===========================================================================================")
print("Menghapus data")
cache = Biodata.pop("Fakultas")
print(Biodata)
print("===========================================================================================")

print(Biodata.get("Fakultas"))
print(cache)