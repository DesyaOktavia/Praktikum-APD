print ("Selamat datang grosir mobil")
print (" Silahkan login terlebih dahulu ")

id = "desya"
pw = "111"
salah = 0

while salah < 3 :
    username = input("Masukkan Username Anda: ")
    password = input("Masukkan Password Anda: ")

    if username == id and password == pw :
        print ("Anda berhasil Login")
        break
    else :
        salah += 1 
        print ("Anda Salah Memasukkan Username atau Password")
if salah < 3 :
    while True :
        merk_mobil = (input("masukkan merk mobil: "))
        print ("""
                Pilihan merek mobil
                    1. Tesla
                    2. Toyota
                    3. Hyundai
            """)
        harga_setiap_merk_mobil = int(input("masukkan harga setiap merk mobil: "))

        diskon_merk_tesla = 0.17
        diskon_merk_toyota = 0.21
        diskon_merk_hyundai = 0.23

        if merk_mobil == 1: 
            harga_diskon_merk_tesla= harga_setiap_merk_mobil * 0.17
            harga_setelah_diskon= harga_setiap_merk_mobil-harga_diskon_merk_tesla
            print("harga setelah diskon merk mobil= ",harga_setelah_diskon)
        elif merk_mobil == 2:
            harga_diskon_merk_toyota= harga_setiap_merk_mobil * 0.21
            harga_setelah_diskon= harga_setiap_merk_mobil-harga_diskon_merk_toyota
            print("harga setelah diskon merk mobil= ",harga_setelah_diskon)
        elif merk_mobil == 3:
            harga_diskon_merk_hyundai= harga_setiap_merk_mobil * 0.23
            harga_setelah_diskon= harga_setiap_merk_mobil-harga_diskon_merk_hyundai
            print("harga setelah diskon merk mobil= ",harga_setelah_diskon)
        else:
            print("Bu Navira tidak jadi membeli mobil")

            print ("""   MENU
                   1. KEMBALI KE PROGRAM 
                   2. KELUAR
                """)
            menu = int (input("Masukkan Pilihan Anda (1/2): "))
            if menu == 1 :
                pass
            elif menu == 2 :
                print("Terima kasih telah telah menggunakan program ini")
                break

if salah == 3 :
    print ("anda gagal login,silahkan coba dilain waktu")