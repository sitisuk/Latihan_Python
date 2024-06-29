
list_nama=[]
list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=1
for i in range(ulang):
    print("data Ke -"+str(i+1))
    list_nama.append(input("Masukan Nama :"))
    list_nim.append(input("Masukkan Nim  :"))
    list_uts.append(int(input("Masukan Nilai UTS  :")))
    list_uas.append(int(input("Masukan Nilai UAS :")))
    #Proses
    for i in range(ulang):
        list_total.append((list_uas[i] + list_uts[i])/2)
    #Cetak
    print("=" * 40)
    print("Nim      Nilai Uts    Nilai UAS     Total ")
    print("=" * 40)
    for i in range(ulang):
        print("%s\t%i\t%i\t%i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
        print("=" * 40)
