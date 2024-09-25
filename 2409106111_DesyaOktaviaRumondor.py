# ulang = 10
# for i in range(ulang):
#     print("Perulangan ke-" + str(i))

# for i in range(2,10):
#     print(f"halo {i}")

# for i in range(10,2,-2):
#     print(f"halo {i}")

# for i in range(2,10,2):
#     print(f"halo {i}")

# for i in range(2,10,3):
#     print(f"halo {i}")
    
# for i in range(2,10,4):
#     print(f"halo {i}")

# for i in range(10):
#     print(f"halo")

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()


#  for adalah untuk kita menentukan perulangan kita mau sampai berapa/mana
# range adalah fungsi membuat kumpulan nilai atau parameter di python secara berurutan
# i adalah isi dari data range
# kalau kita menginginkan nilai nya stop di 9 maka batas atas itu adalah 10
# kalau batas atas 4 maka nilai akan stop di nilai 3


# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}") (sama seperti yang dibawah)

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung = hitung + 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}") (sama seperti yang diatas)

# while True:
#     print("halo")

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Mengulang? ")
#     if ulang == "tidak" or ulang =="Tidak":
#         break
# print(f"Total Perulangan: {hitung}")

# while True:
#     print("halo")
#     break

# print(“Daftar bilangan ganjil dari 1-10”)
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# while True:
#     print("halo")
#     continue 
#     print("fufufafa") (tidak bisa diprint)

# while True:
#     print("halo")
#     print("fufufafa")
#     continue (dapar di run)

# print('Daftar bilangan genap dari 1-10')
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i)

# print('Daftar bilangan ganjil dari 1-10')
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i)

while digunakan apabila kita ingin terus-menerus menginput dan tidak ingin berhenti
for digunakan apabila kita ingin mengeprint dengan satu-satu
i dimulai dari 0 sendangkan i+1 maka output yang keluar akan dimulai dari 1
len adalah jumlah panjang list

kelasC=["melchi", 2409106117]
for i in range(len(kelasC)):
    print(f"{i}. {kelasC[i]"})
print(kelasC)
