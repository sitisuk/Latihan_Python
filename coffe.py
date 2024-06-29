def main(): 
    while True :
        #Daftar Menu Nostalgia Coffee Shop
        menu = {
            'ice cappucino' : 18000,
            'americano' : 12000,
            'caramel' : 16000,
            'hazelnut' : 20000,
        }

        #Input nama pembeli
        nama_pembeli = input("Masukan Nama Pembeli : ")

        #List untuk menyimpan pilihan minuman dan jumlahnya
        pesanan = []

        #Input minuman yang dibeli dan jumlahnya
        while True :
            print("n/Pilih minuman yang di beli (ketik 'selesai' untuk mengakhiri) : ")
            for key in menu :
                print(f"{key.capitalize()}: Rp {menu[key]}")

            minuman_input = input("/nMasukan nama minuman atau ketik 'selesai : ").strip().lower()

            if minuman_input == 'selesai' :
                break
            
            if minuman_input in menu :
                while True :
                    try:
                        jumlah = int(input(f"Masukan jumlah {minuman_input} :"))
                        if jumlah > 0 :
                            pesanan.append((minuman_input, jumlah))
                            break
                        else:
                            print("Jumlah harus lebih dari 0.")
                    except ValueError:
                        print("Masukan jumlah dalam angka.")
            else:
                print("Minuman tidak tersedia. Silahkan pilih dari menu yang tersedia.")

        #Hitung total harga untuk semua pesanan
        total_harga = 0
        for minuman, jumlah in pesanan :
            harga_per_item = menu[minuman]
            total_harga +=  harga_per_item * jumlah

        #Diskon 5% jika pembelian di atas Rp 50000
        if total_harga > 50000:
            diskon = 0.05 * total_harga
        else:
            diskon = 0

        #Hitun total setelah diskon
        total_setelah_diskon = total_harga - diskon

        #Hitung PPN 10%
        ppn = 0.01 * total_setelah_diskon

        #Hitung total harga akhir (setelah diskon dan ditambah PPN)
        total_akhir = total_setelah_diskon + ppn

        #Tampilkan struk pembayaran
        print("/n           Struk Pembayaran            ")
        print("           Nostalgia Coffee Shop          ")
        print("= * 40")
        print(f"Nama Pembeli           :{nama_pembeli}")
        print("Minuman yang di pesan   :")
        for minuman, jumlah in pesanan:
            print(f"{minuman.capitalize()} x {jumlah}")
        print("-----------------------------------------")
        print(f"Total Harga             : Rp {total_harga}")
        if diskon > 0 :
            print(f"Diskon 5%               : Rp {diskon}")
        print(f"PPN 10 %                : Rp {ppn}")
        print(f"Total Bayar             : Rp {total_akhir}")

        #Input uang bayar dan hitung kembalian
        while True:
            try:
                uang_bayar = float(input("/nUang Bayar            :Rp "))
                if uang_bayar >= total_akhir:
                    break
                else: 
                    print("Uang yang dibayarkan kurang.")
            except ValueError:
                print("Masukan jumlah uang dalam angka.")

        uang_kembali = uang_bayar - total_akhir
        print(f"Uang kembali            : Rp {uang_kembali}")

        #Tanya apakah akan bertansaksi lagi
        transaksi_lagi = input("/nApakah akan melakukan transaksi lagi? (ya/tidak): ").lower()
        if transaksi_lagi != 'ya' :
            print("Terima kasih telah berbelanja di Nostalgia Coffe Shop!")
            break

if __name__ == "__main__" :
    main()




            
        