print("        SEAFOOD BAROKAH   ")
print("------------------------------")
print("kode list  jenis menu     harga")
print("-----------------------------")
print("U        Udang        Rp. 30000")
print("C        Cumi         Rp. 25000")
print("I        Ikan         Rp. 15000")
print("K        Kepiting     Rp. 45000")
print("-----------------------------")

banyak_jenis = int(input("Banyak Jenis : "))
kode_list = []
banyak_beli= []
jenis_seafood = []
harga = []
jumlah = []

i= 0
while i<banyak_seafood:
    print("Jenis Ke - ", i+1)
    kode_list.append(input("Kode [U/C/I/K] : "))
    banyak_beli.append(int(input("Banyak_beli : ")))

    if kode[i] == "U" or kode[i] == "u" :
        jenis_seafood.append("Udang")
        harga.append("30000")
        jumlah.append(banyak_beli[i]*int("30000"))
    elif kode[i] == "C" or kode[i] == "c" :
        jenis_seafood.append("Cumi")
        harga.append("25000")
        jumlah.append(banyak_beli[i]*int("25000"))
    elif kode[i] == "I" or kode[i] == "i" :
        jenis_seafood.append("Ikan")
        harga.append("15000")
        jumlah.append(banyak_beli[i]*int("15000"))
    else :
        jenis_seafood.append("Kode Salah")
        harga_paketappend("0")
        jumlah.append(banyak_beli[i]*int("0"))     
    i= i + 1

print("           SEAFOOD BAROKAH             ")
print("-------------------------------------------")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Seafood   paket        Beli      Harga ")
print("--------------------------------------------")

a = 0
while a < banyak_jenis:
    print("%i    %s       %s        %i         %i" % (a+1,jenis_seafood[a], harga[a], banyak_beli[a], jumlah[a]))
    a = a + 1

print("--------------------------------------------")
jumlah_bayar = int(input("Jumlah Bayar : Rp.", ))
pajak = jumlah_bayar * 0.1 
total_bayar = jumlah_bayar + pajak
print("Pajak 10 %   :Rp. ", pajak)
print("Total Bayar  :Rp. ", total_bayar)
print("--------------------------------------------")