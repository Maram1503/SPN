def rotate16(key,position):
    k=((key<<position)|(key>>(16-position)))&0xFFFF
    return k


def generer_sous_cles(key):
    k1=key>>8
    k2=key&0xFF
    k3=rotate16(key,3)>>8
    k4=rotate16(key,5)>>8
    k5=rotate16(key,7)>>8
    return k1,k2,k3,k4,k5
print(generer_sous_cles(0xCA61)[0])