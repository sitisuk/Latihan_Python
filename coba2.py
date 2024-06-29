def main():
    # Daftar menu beserta harga
    menu = {
        'mie hompimpa': 10000,
        'mie gacoan': 12000,
        'mineral': 4000,
        'es teh': 5000
    }

    # Input nama dan nomor meja
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    nomor_meja = input("Masukkan nomor meja: ")

    # Input pesanan
    pesanan = []
    total_harga = 0

    while True:
        print("\nDaftar Menu:")
        for key, value in menu.items():
            print(f"{key}: Rp {value}")

        pesanan_menu = input("\nMasukkan menu yang ingin dipesan (selesai untuk mengakhiri): ")
        if pesanan_menu.lower() == 'selesai':
            break
        elif pesanan_menu.lower() in menu:
            jumlah_pesan = int(input(f"Masukkan jumlah {pesanan_menu}: "))
            harga_menu = menu[pesanan_menu] * jumlah_pesan
            pesanan.append((pesanan_menu, jumlah_pesan, harga_menu))
            total_harga += harga_menu
        else:
            print("Menu tidak valid. Silakan coba lagi.")

    # Hitung diskon jika total harga pembelian di atas 50,000
    diskon = 0
    if total_harga > 50000:
        diskon = min(0.1 * total_harga, 5000)  # Diskon maksimal 5000

    # Hitung total yang harus dibayar setelah diskon
    total_setelah_diskon = total_harga - diskon

    # Cetak struk pembayaran
    print("\n===== Struk Pembayaran =====")
    print(f"Pelanggan: {nama_pelanggan}")
    print(f"Nomor Meja: {nomor_meja}")
    print("----------------------------")
    for pesanan_menu, jumlah_pesan, harga_menu in pesanan:
        print(f"{pesanan_menu}: {jumlah_pesan} x Rp {menu[pesanan_menu]} = Rp {harga_menu}")
    print("----------------------------")
    print(f"Total Harga: Rp {total_harga}")
    if diskon > 0:
        print(f"Diskon 10% (maksimal Rp 5000): Rp {diskon}")
    print(f"Total yang harus dibayar: Rp {total_setelah_diskon}")
    print("============================")

