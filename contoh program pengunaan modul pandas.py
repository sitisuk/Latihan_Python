import pandas as pd
#variabel yang berulang menggunakan list/matriks
list_nim=[]
list_nama=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang = 2

for i in range(ulang):
    print("data ke - " + str(i+1))
    list_nim.append(input("Nim: "))
    list_nama.append(input("Nama: "))
    list_uts.append(int(input("nilai uts: ")))
    list_uas.append(int(input("nilai uas: ")))
#proses
for i in range(ulang):
    list_total.append((list_uas[i]+list_uts[i])/2)

tamu ={
    "Nim :": list_nim,
    "Nama lengkap:": list_nama,
    "Nilai uts:": list_uts,
    "Nilai uas:": list_uas,
    "rata rata:": list_total,
}
data_tamu = pd.DataFrame(tamu)
#cetak
print("=========================Daftar Nilai=========================")
print(data_tamu)
print("===============================================================")

