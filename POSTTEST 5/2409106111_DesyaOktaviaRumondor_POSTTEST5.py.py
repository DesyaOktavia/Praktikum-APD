akuns = [
    #username, password, role
    ['desya', 'jemaatku', 'admin'],
    ['desya', 'jemaatku', 'admin']
]
Jemaat = []
Users = ['Admin', 'Jemaat']
Pengguna = [ ]

while True :
    print("======================================================================")
    print("                       Halo! Syalom anak Tuhan😇                     ")
    print("               ✨ Selamat Datang Di Aplikasi Jemaat-Ku✨             ")
    print("======================================================================")
    print("    Kami hadir disini untuk membantu data-data yang anda simpan😉    ")
    print("======================================================================")
    print(" ")
    print("--------Apakah anda sudah memiliki akun?------")
    print("1. Daftar, Belum Memiliki")
    print("2. Login, Sudah Memiliki")
    print("3. Exit")
    print("______________________________________________")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1" :
        print("===============================================================")
        print("Halo Pengguna baru! Silahkan Masukkan Data Anda Dengan Benar😊")
        print("===============================================================")
        new_username = input("Username: ")
        new_password= input("Password: ")
        role = input("Masukkan role (Admin/Jemaat): ")

        if new_username in akuns :
            print("Username yang anda pakai sudah ada, silakan pilih username lain.")
        else :
            akuns.append([new_username, new_password, role])
            print(f"Selamat Akun Anda Sudah Terdaftar, Selamat Datang {new_username}😊!.")
        continue

    elif opsi == '2' :
        print("-----Syalom, Silahkan Masukkan Akun Anda😊!-----")
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")

        for akun in akuns :
            if akun[1] == password :
                Pengguna = akun
                print(f"Selamat datang {username}, anda telah berhasil login😊!")
                break
        if len(Pengguna) == 0 :
            print("Username atau password yang anda masukkan salah, silahkan coba lagi.")

        while Pengguna :
            print("\n----- SILAHKAN PILIH MENU -----")
            print("1. Lihat Data Jemaat")
            print("2. Tambah Data Jemaat")
            if 'admin' == Pengguna[2] :
                print("3. Update Data Jemaat")
                print("4. Hapus Data Jemaat")
            print("5. Logout")
            opsi = input("Pilih menu: ")

            if opsi == '1' :
                if len(Jemaat) == 0:
                    print("Belum ada data jemaat.")
                else:
                    print("\n========== Data Jemaat yang Terdaftar ==========")
                    for index, data in enumerate(Jemaat):
                        print(f"{index + 1}. Nama lengkap: {data[0]}, Tempat Tanggal Lahir: {data[1]} Umur: {data[2]}, Status Kawin: {data[3]}, Alamat: {data[4]}")

            elif opsi == '2':
                nama_lengkap = input("Masukkan nama anda: ")
                tempat_tanggal_lahir = input("Masukkan tempat tanggal lahir anda: ")
                umur = input("Masukkan umur anda: ")
                status_kawin = input("Masukkan kawin/belum kawin: ")
                alamat = input("Masukkan alamat jemaat: ")
                Jemaat.append([nama_lengkap, tempat_tanggal_lahir, umur, status_kawin, alamat])
                print("\n========== Data Jemaat Telah Berhasil Ditambahkan ==========")

            elif opsi == '3' and Pengguna[2] == "admin" :
                if len(Jemaat) == 0:
                    print("Belum ada data jemaat, silahkan mengisi data jemaat terlebih dahulu.")
                else:
                    print("\n========== Data Jemaat yang Terdaftar ==========")
                    for index, data in enumerate(Jemaat) :
                        print(f"{index + 1}. Nama lengkap: {data[0]}, Tempat Tanggal Lahir: {data[1]} Umur: {data[2]}, Status Kawin: {data[3]}, Alamat: {data[4]}")

                    update_index = int(input("Masukkan nomor jemaat yang ingin diupdate: ")) - 1
                    
                    if 0 <= update_index < len(Jemaat) :
                        nama_lengkap_baru = input("Masukkan nama anda: ")
                        tempat_tanggal_lahir_baru = input("Masukkan tempat tanggal lahir anda: ")
                        umur_baru = input("Masukkan umur anda: ")
                        status_kawin_baru = input("Masukkan kawin/belum kawin: ")
                        alamat_baru = input("Masukkan alamat jemaat: ")
                        Jemaat[update_index] = [nama_lengkap_baru, tempat_tanggal_lahir_baru, umur_baru, status_kawin_baru, alamat_baru]
                        print("Data jemaat telah berhasil di perbaharui.")
                    else :
                        print("Nomor jemaat tidak valid.")

            elif opsi == '4' and Pengguna[2] == "admin" :
                if len(Jemaat) == 0:
                    print("Belum ada data jemaat untuk dihapus.")
                else :
                    print("\n========== Data Jemaat yang Terdaftar ==========")
                    for index, data in enumerate(Jemaat):
                        print(f"{index + 1}. Nama lengkap: {data[0]}, Tempat Tanggal Lahir: {data[1]} Umur: {data[2]}, Status Kawin: {data[3]}, Alamat: {data[4]}")
                    
                    delete_index = int(input("Masukkan nomor jemaat yang ingin dihapus: ")) - 1
                    
                    if 0 <= delete_index < len(Jemaat):
                        Jemaat.pop(delete_index)
                        print("Data jemaat telah berhasil dihapus.")
                    else:
                        print("Nomor jemaat tidak valid.")

            elif opsi == '5' :
                print("Apakah anda yakin mau logout dari aplikasi?.")
                print("1. Iya")
                print("2. Tidak")
                opsi = input("Input pilihan: ")
                print(" ")

                if opsi == "1" :
                    print("Terimakasih sudah menggunakan aplikasi jemaat-ku, semoga harimu menyenangkan!")
                    break
                elif opsi == "2"  :
                    continue
                else:
                    print("Input tidak valid, silahkan pilih '1' atau '2'\n")
                    break

    elif opsi == "3" :
        print("Apakah kamu yakin ingin keluar dari aplikasi? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi jemaat-ku, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else :
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
            
    else :
            print("Pilihan tidak valid atau akses terbatas.")