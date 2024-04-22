#input
pembeli=input("Input Nama Pembeli :")
no_hp=input("Input No. Handphone :")
jurusan=input("Input Jurusan [SBY/BL/LMP] :")
#Proses
if jurusan=="SBY" :
    namajurusan="Surabaya"
    harga =300000
elif jurusan=="BL" :
    namajurusan="Bali"
    harga=350000
else :
    namajurusan=="Lampung" 
    harga="500000"

#input jumlah beli
jumlah=int(input("Masukan Jumlah Beli : "))

#proses potongan
if jumlah>=3 :
    potongan=(jumlah*harga)*0.1
    total=(jumlah*harga)-potongan
else :
    potongan =0
    total=(jumlah*harga)-potongan

#cetak hasil
print("--------------------------------------")
print("     PENJUALAN TIKET BUS")
print("            XYZ")
print("--------------------------------------")
print("Nama Pembeli         : " +str(pembeli))
print("No. Handphone        : " +str(no_hp))
print("Kode Jurusan yang dipilih :" +str(jurusan))
print("Nama Kota Tujuan     : "+str(namajurusan))
print("Harga                :",+(harga))
print("Jumlah Beli          :",+(jumlah))
print("--------------------------------------")
print("Potongan yang di dapat :",+(potongan))
print("Total Bayar           :",+(total))
ubay=int(input("Masukan Uang Bayar:"))
uangkembali=int(input("ubay-total :"))
print("Uang Kembali :",+uangkembali)


