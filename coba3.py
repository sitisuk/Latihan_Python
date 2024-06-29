# define the initial balance
saldo_awal = 500000

#define the prices of the pulsa
harga_pulsa = {
    5000 : 7000,
    10000 : 12000,
    20000 : 22000,
    25000 : 27000,
    50000 : 52000,
    100000 : 102000,
}
#discount for purchase over Rp. 50.000
diskon = 2000

#Funcion to process a pulsa purchase
def beli_pulsa(saldo, harga): 
    if harga in harga_pulsa :
        bayar = harga_pulsa[harga]
        if bayar > 50000 :
            bayar -= diskon
        if saldo >= bayar :
            saldo -= bayar
            print(f"Pembelian Berhasil!")
        saldo_tersisa : Rp[saldo]
    else:
     print ("saldo tidak cukup")
    return saldo

#main program
def main():
    saldo = saldo_awal
    while True :
        print(f"/nSaldo saat ini : Rp.{saldo}")
        nama = input("masukan nama pelanggan : ")
        nomor_hp = input("masukan nomor handphone: ")
        try :
            nominal_pulsa = int(input("masukan nominal pulsa (5000,10000,20000,25000,50000,100000):"))
        except ValueError:
            print("nominal pulsa harus berupa angka!")
            continue
        saldo = beli_pulsa(saldo,nominal_pulsa)
        lanjut = input("apakah ingin melanjutkan transaksi? (y/n : ").lower()
        if lanjut != 'y' :
            break
    print("Terimaksih telah menggunakan layanan kami!")

# run the main program
if __name__ == "__main__" :
    main()
