#Perhitungan luas segiempat,segitiga,lingkaran
#l = lebar segiempat
#p = panjang segiempat
#a = alas segitiga
#t = tinggi segitiga
#r = jari-jari lingkaran
#pi = 3.14

print("==============================================")
l = int(input("masukan lebar segiempat :"))
p = int(input("masukan panjang segiempat :"))
luas_segiempat = p * l
print("luas segiempat adalah",str(luas_segiempat))
print("===============================================")

print("================================================")
a = int(input("masukan alas segitiga :"))
t = int(input("masukan tinggi segitiga :"))
luas_segi_tiga = 0,5 * a * t
print("luas segitiga adalah", str(luas_segi_tiga))
print("=================================================")

print("==================================================")
r = int (input("masukan jari-jari lingkaran :"))

luas_lingkaran = 3.14 *r*r
print("luas lingkaran adalah :",luas_lingkaran)
print("==================================================")



