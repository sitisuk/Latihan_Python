Nama    :Siti Sukaesih
Nim     :19235071
Kelas   :19.1A.24



#input data karyawan
karyawan=input("masukan nama karyawan :")
jabatan=input("masukan golongan jabatan [1/2/3] :")
pendidikan=input("masukan pendidikan karyawan [SMA/D1/D3/S1] :")
jam_kerja=int(input("masukan jumlah jam kerja :"))
gaji_pokok=300000

#proses jabatan
if jabatan=="1" :
    presentase="5%"
    tunjangan_jab= 5* 300000 
elif jabatan=="2" :
    presentase="10%"
    tunjangan_jab=10 * 300000 
elif jabatan== "3":
    presentase="15%"
    tunjangan_jab=15 * 300000 
   
else:
    tunjangan_jab== 0


#hitung tunjangan pendidikan
if pendidikan == "SMA" :
    presentase="2.5%"
    tunjangan_pen= 2.5 * 300000 
elif pendidikan== "D1" :
    presentase="5%"
    tunjangan_pen= 5 * 300000 
elif pendidikan=="D3" :
    presentase=="20%"
    tunjangan_pen= 20 * 300000 
elif pendidikan=="S1" :
    presentase=="30%"
    tunjangan_pen= 30 * 300000 
else:
     tunjangan_pendidikan= 0

#proses jam kerja
#di atas 8 jam di hitung lembur

if jam_kerja > 8:
    jam_kerja=(jam_kerja - 8) * 3500 

#di bawah 8 jam tidak di hitung lembur

else :
    jam_kerja= 0

#output
print("========================================")
print("Karyawan yang bernama :",str(karyawan ))
print("Honor yang di terima")
print("Tunjangan Jabatan       Rp. :",str(tunjangan_jab))
print("Tunjangan Pendidikan    Rp. :",str(tunjangan_pen))
print("Honor Lembur            Rp. :",str(jam_kerja))
print("Gaji Pokok              Rp. :",str(gaji_pokok))
print("                             ______________+")
total_gaji=int(gaji_pokok) + int(tunjangan_jab)+ int(tunjangan_pen) + int(jam_kerja)
print("Total Gaji              Rp. :",(total_gaji))
