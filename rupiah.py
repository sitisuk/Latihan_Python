#rupiah.py

import locale

def rupiah_format(angka, with_prefix=False, desimal=2) :
    locale.setlocale(locale.LC_NUMBERIK, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    if whit_prefix:
        return "Rp. {}".format(rupiah)
    return rupiah