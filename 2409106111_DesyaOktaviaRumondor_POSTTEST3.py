merk_mobil = str(input("masukkan merk mobil: "))
harga_setiap_merk_mobil = int(input("masukkan harga setiap merk mobil: "))

diskon_merk_tesla = 0.17
diskon_merk_toyota = 0.21
diskon_merk_hyundai = 0.23

if merk_mobil == "tesla": 
    harga_diskon_merk_tesla= harga_setiap_merk_mobil * 0.17
    harga_setelah_diskon= harga_setiap_merk_mobil-harga_diskon_merk_tesla
    print("harga setelah diskon merk mobil= ",harga_setelah_diskon)
elif merk_mobil == "toyota":
    harga_diskon_merk_toyota= harga_setiap_merk_mobil * 0.21
    harga_setelah_diskon= harga_setiap_merk_mobil-harga_diskon_merk_toyota
    print("harga setelah diskon merk mobil= ",harga_setelah_diskon)
elif merk_mobil == "Hyundai":
    harga_diskon_merk_hyundai= harga_setiap_merk_mobil * 0.23
    harga_setelah_diskon= harga_setiap_merk_mobil-harga_diskon_merk_hyundai
    print("harga setelah diskon merk mobil= ",harga_setelah_diskon)
else:
    print("Bu Navira tidak jadi membeli mobil")
    