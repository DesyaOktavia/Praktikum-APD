nama = input("masukan nama: ")
nim = input("nim: ")
harga_merk_mobil = float(input("masukan harga merk mobil: "))

harga_diskon_merk_mobil_tesla = 0.17
harga_diskon_merk_mobil_toyota = 0.21
harga_diskon_merk_mobil_hyundai = 0.23

harga_tesla_setelah_diskon= harga_merk_mobil * (1 - harga_diskon_merk_mobil_tesla)
modulus_7_tesla = harga_merk_mobil % 7
harga_toyota_setelah_diskon= harga_merk_mobil * (1 - harga_diskon_merk_mobil_toyota)
modulus_7_toyota = harga_merk_mobil % 7
harga_hyundai_setelah_diskon= harga_merk_mobil * (1 - harga_diskon_merk_mobil_hyundai)
modulus_7_hyundai = harga_merk_mobil % 7

print(f"mobil tesla seharga {harga_merk_mobil} diskon 17% menjadi{harga_tesla_setelah_diskon:.2f},"
      f"mobil toyota seharga {harga_merk_mobil} diskon 21% menjadi{harga_toyota_setelah_diskon:.2f},"
      f"mobil hyundai seharga {harga_merk_mobil} diskon 23% menjadi{harga_hyundai_setelah_diskon:2f}")
print(f"modulus 7 dari harga tesla adalah{modulus_7_tesla:.2f},"
      f"modulus 7 dari harga toyota adalah{modulus_7_toyota:.2f},"
      f"modulus 7 dari harga hyundai adalah{modulus_7_hyundai:.2f},")
0