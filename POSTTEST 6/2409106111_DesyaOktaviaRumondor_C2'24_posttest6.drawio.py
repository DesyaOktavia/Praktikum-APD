akuns = {
    'desya': {'password': 'jemaatku', 'role': 'admin'},
}

Jemaat = {}
Users = {'Admin', 'Jemaat'}
Pengguna = {}

while True:
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

    if opsi == "1":
        print("===============================================================")
        print("Halo Pengguna baru! Silahkan Masukkan Data Anda Dengan Benar😊")
        print("===============================================================")
        new_username = input("Username: ")
        new_password = input("Password: ")
        role = input("Masukkan role (Admin/Jemaat): ")

        if new_username in akuns:
            print("Username yang anda pakai sudah ada, silakan pilih username lain.")
        else:
            akuns[new_username] = {'password': new_password, 'role': role}
            print(f"Selamat Akun Anda Sudah Terdaftar, Selamat Datang {new_username}😊!.")
        continue

    elif opsi == '2':
        print("-----Syalom, Silahkan Masukkan Akun Anda😊!-----")
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")

        if username in akuns and akuns[username]['password'] == password:
            Pengguna = {'username': username, 'role': akuns[username]['role']}
            print(f"Selamat datang {username}, anda telah berhasil login😊!")
        else:
            print("Username atau password yang anda masukkan salah, silahkan coba lagi.")
            continue

        while Pengguna:
            print("\n----- SILAHKAN PILIH MENU -----")
            print("1. Lihat Data Jemaat")
            print("2. Tambah Data Jemaat")
            if Pengguna['role'] == 'admin':
                print("3. Update Data Jemaat")
                print("4. Hapus Data Jemaat")
            print("5. Logout")
            opsi = input("Pilih menu: ")

            if opsi == '1':
                if len(Jemaat) == 0:
                    print("Belum ada data jemaat.")
                else:
                    print("\n========== Data Jemaat yang Terdaftar ==========")
                    for jemaat_id, data in Jemaat.items():
                        print(f"ID: {jemaat_id}, Nama lengkap: {data['nama_lengkap']}, Tempat Tanggal Lahir: {data['ttl']}, Umur: {data['umur']}, Status Kawin: {data['status_kawin']}, Alamat: {data['alamat']}")

            elif opsi == '2':
                jemaat_id = input("Masukkan ID jemaat: ")
                nama_lengkap = input("Masukkan nama lengkap: ")
                tempat_tanggal_lahir = input("Masukkan tempat tanggal lahir: ")
                umur = input("Masukkan umur: ")
                status_kawin = input("Masukkan kawin/belum kawin: ")
                alamat = input("Masukkan alamat jemaat: ")

                Jemaat[jemaat_id] = {
                    'nama_lengkap': nama_lengkap,
                    'ttl': tempat_tanggal_lahir,
                    'umur': umur,
                    'status_kawin': status_kawin,
                    'alamat': alamat
                }
                print("\n========== Data Jemaat Telah Berhasil Ditambahkan ==========")

            elif opsi == '3' and Pengguna['role'] == 'admin':
                if len(Jemaat) == 0:
                    print("Belum ada data jemaat, silahkan mengisi data jemaat terlebih dahulu.")
                else:
                    print("\n========== Data Jemaat yang Terdaftar ==========")
                    for jemaat_id, data in Jemaat.items():
                        print(f"ID: {jemaat_id}, Nama lengkap: {data['nama_lengkap']}, Tempat Tanggal Lahir: {data['ttl']}, Umur: {data['umur']}, Status Kawin: {data['status_kawin']}, Alamat: {data['alamat']}")

                    update_id = input("Masukkan ID jemaat yang ingin diupdate: ")
                    
                    if update_id in Jemaat:
                        nama_lengkap_baru = input("Masukkan nama baru: ")
                        tempat_tanggal_lahir_baru = input("Masukkan tempat tanggal lahir baru: ")
                        umur_baru = input("Masukkan umur baru: ")
                        status_kawin_baru = input("Masukkan kawin/belum kawin: ")
                        alamat_baru = input("Masukkan alamat baru: ")

                        Jemaat[update_id] = {
                            'nama_lengkap': nama_lengkap_baru,
                            'ttl': tempat_tanggal_lahir_baru,
                            'umur': umur_baru,
                            'status_kawin': status_kawin_baru,
                            'alamat': alamat_baru
                        }
                        print("Data jemaat telah berhasil diperbarui.")
                    else:
                        print("ID jemaat tidak valid.")

            elif opsi == '4' and Pengguna['role'] == 'admin':
                if len(Jemaat) == 0:
                    print("Belum ada data jemaat untuk dihapus.")
                else:
                    print("\n========== Data Jemaat yang Terdaftar ==========")
                    for jemaat_id, data in Jemaat.items():
                        print(f"ID: {jemaat_id}, Nama lengkap: {data['nama_lengkap']}, Tempat Tanggal Lahir: {data['ttl']}, Umur: {data['umur']}, Status Kawin: {data['status_kawin']}, Alamat: {data['alamat']}")

                    delete_id = input("Masukkan ID jemaat yang ingin dihapus: ")
                    
                    if delete_id in Jemaat:
                        del Jemaat[delete_id]
                        print("Data jemaat telah berhasil dihapus.")
                    else:
                        print("ID jemaat tidak valid.")

            elif opsi == '5':
                print("Apakah anda yakin mau logout dari aplikasi?")
                print("1. Iya")
                print("2. Tidak")
                opsi_logout = input("Input pilihan: ")
                print(" ")

                if opsi_logout == "1":
                    print("Terimakasih sudah menggunakan aplikasi jemaat-ku, semoga harimu menyenangkan!")
                    break
                elif opsi_logout == "2":
                    continue
                else:
                    print("Input tidak valid, silahkan pilih '1' atau '2'\n")
                    break

    elif opsi == "3":
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
            else:
                print("Input tidak valid, silahkan pilih '1' atau '2'\n")

    else:
        print("Pilihan tidak valid atau akses terbatas.")
