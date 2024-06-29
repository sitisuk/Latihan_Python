#10-50 = kurang
#50-70 = cukup
#70-85 = baik
#>85 = sangat baik

nilai = int(input("masukan nilai" :))
    if nilai < 10 or nilai > 100 :
        return " nilai tidak valid"
    elif nilai <=50 :
        return "kurang"
    elif nilai <=70 :
        return "cukup"
    elif nilai >=80 :
        return "baik"
    elif nilai >=85 :
        return "sangat baik"
    else :
        return "tidak masuk dalam kategori ya