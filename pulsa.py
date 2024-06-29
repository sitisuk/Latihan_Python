saldo = 1000000
lanjut_beli = "y"
user = ("masukan username anda :") and password = ("masukan password anda :")
loggend = "gagal"

def beli_pulsa(p) :
    global saldo
    if saldo >=int(p):
        saldo -=int(P)
        print("anda berhasil membeli pulsa Rp.", p)
        print("sisa saldo anda adalah Rp.", saldo)
    else :
        print("oops saldo anda tidak cukup")
while loggend == "gagal" :
    print("mau beli pulsa silahkan log in")
    username = input("masukan username : ")
    password = input("masukan password : ")
    if username == user['username'] :
       password ==user['password'] :
        print("selamat datang"+user['username'])
        loggend = "berhasil"
    else :
        print("oops username/password anda salah")
    
while lanjut_beli =="y" and loggend =="berhasil" :
    print("beli pulsa")
    print("1, beli pulsa Rp. 5.000")
    print("2, beli pulsa Rp. 10.000")
    print("3, beli pulsa Rp. 20.000")
    print("4, beli pulsa custem")
    print("5, keluar aplikasi")
    a = int(input("silahkan pilih pulsa yang mau di beli : "))
    if a == 1:
        beli_pulsa(5000)
    elif a == 2 :
        beli_pulsa(10000)
    elif a == 3 :
        beli_pulsa(20000)
    elif a == 4 :
        beli_pulsa(input("silahkan masukan nominal pulsa yang akan diisi Rp. "))
    elif a == 5 :
        lanjut_beli = "n"
    else :
        print("pilihan tidak tersedia")
        lanjut_beli =input("mau isi lagi??? (y/n)")