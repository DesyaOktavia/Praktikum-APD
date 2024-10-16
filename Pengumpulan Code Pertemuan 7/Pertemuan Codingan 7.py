#kegunaan import os adalah guna mempermudah kita dalam menggunakan codingan

# #Fungsi dan prosedur => DEF
# #Fungsi utama yaitu dapat menulis/memunculkan deklarasi secara berulang-ulang
# #identasi penulisan di dalam sehabis tanda petik ":"


# #def fungsi tanpa parameter:
# def mhs() :
#     print("Hello")


# def kali():
#     x = 6*4
#     print(x)

# kali()
# kali()
# kali()
# kali()
# #(prosedur penyebutan yang berulang-ulang)


# #def fungsi (parameter)

# def luas_persegi_panjang(panjang, lebar):           #(panjang, lebar) = parameter
#     luas = panjang * lebar

# print ("Luas persegi panjang:", luas)
# print ("Luas persegi panjang:", luas)

# luas_persegi_panjang(4, 6) #Diisi sesuai dengan banyaknya value yang di intruksikan   #(4,6) = argumen



# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# luas_persegi(4) #hanya memberi perintah bahwa nilai tersebut sesuai dengan yang di mau

# hasil = luas_persegi(4) + luas_persegi(2)
# print(hasil)

# def luas_persegi(sisi): #tipe data tuple
#     luas = sisi * sisi
#     jumlah = sisi + sisi
#     return luas, jumlah

# luas, jumlah = (luas_persegi)


# def mhs(nama, nim, *arr): #karena ada bintang jadi data tersebut dapat tersimpan  #harus ditaruh di akhir parameter dan variabelnya bebas
#     print(nama)
#     print(nim)
#     print(arr)

# mhs("ucup", "20", 1,2,3,4,5,) #tipe data kolektif => list, tuple, dictionary


# def mhs(nama, nim, nilai): 
#     print(nama)
#     print(nim)
#     print(nilai)

#     mhs("ucup", "20", 40 )


#list tidak menggunakan bintang
# #bintang 1 => tuple
# #bintang 2 => dictionary


# def mhs(nama, nim, **arr): 
#     print(nama)
#     print(nim)
#     print(nilai)

#     mhs("ucup", "20", data = 2, data2 = 3)
# #kita dapat memakai return di dalam fungsi itu sendiri (def parameter)


# def nilai(angka) :
#     if angka > 10:
#         print("1")
#         return
#     else:
#         print("2")
#         return
#     print("3")


# def nilai(angka) :
#     if angka > 10:
#         print("1")
#         # return
#     else:
#         print("2")
#         # return
#     print("3")

# nilai(10)


#menggunakan fungsi itu saat kita melihat kode nya itu di ulang atau tidak
#jika kodenya di ulang, maka gunakan fungsi. meskipun kode tersebut memiliki arti yang berbeda

#scoop 
#perbedaan variabel lokal dan global:
    #variabel global adalah
    #valiabel lokal adalah 


#variabel lokal dan global
# data = 10 #variabel global

# def nilai():
#     data = 20   #variabel lokal
#     print(data)    #akan print variabel lokal
# #perhatikan identasi (keluar->dalam)

# # kecuali:
# nilai()
# print(data) #akan print variabel global


def data(kumpulan):
    print(kumpulan)

value = [1,2,3,4]
data(value)
#kenapa print kumpulan dapat menghasilkan value?
#karena value sebagai argumen mengisi di kumpulan sebagai parameter maka otomatis value akan mengisi ke kumpulan


#tuple sangat digunakan untuk menjaga keamanan program


#bagaimana mengeprint argumen 
def mhs(nama1, nama2, nama3):
    print(nama3)

mhs(nama3= "ucup", nama2= "saipul", nama1="michael")

