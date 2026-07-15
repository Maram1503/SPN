import SBox,key_schedule,Permutation
def sub_octet(bloc):
    sup=bloc>>4
    inf=bloc&0xF
    return SBox.substituer(sup)<<4|SBox.substituer(inf)
print(sub_octet(0xAB))


def inv_sub_octet(bloc):
    sup=bloc>>4
    inf=bloc&0xF
    return SBox.inv_sbox(sup)<<4|SBox.inv_sbox(inf)
print(inv_sub_octet(61))
print(0xAB)



def round_normal(bloc,sub_key):
    return(Permutation.permuter(sub_octet(bloc^sub_key)))



def round_final(bloc,k4,k5):
    return k5^sub_octet(bloc^k4)



def chiffrememnt_bloc(bloc,key):
    keys=key_schedule.generer_sous_cles(key)
    for i in range(1,4):
        bloc=round_normal(bloc,keys[i-1])
    return round_final(bloc,keys[3],keys[4])



def dechiffrement_bloc(bloc,key):
    keys=key_schedule.generer_sous_cles(key)
    bloc=inv_round_final(bloc,keys[3],keys[4])
    for i in range(3,0,-1):
        bloc=inv_round_normal(bloc,keys[i-1])
    return bloc


def inv_round_final(bloc,k4,k5):
    return(inv_sub_octet(bloc^k5)^k4)

def inv_round_normal(bloc,sub_key):
    return(inv_sub_octet(Permutation.inv_permuter(bloc))^sub_key)

def chiff_msg(msg,key):
    if (msg == "") or not isinstance(msg,str):
        raise ValueError("Message Vide!!")
    octets=msg.encode("UTF-8")
    resultat_hex=""
    for octet in octets:
        bloc_chiffre=chiffrememnt_bloc(octet,key)
        resultat_hex+=format(bloc_chiffre,"02x")
    return resultat_hex
def dechiff_msg(msg,key):
    octets_dechiffres = []
    for i in range(0, len(msg), 2):  
        morceau_hex = msg[i:i+2]
        octet = int(morceau_hex, 16)
        octets_dechiffres.append(dechiffrement_bloc(octet, key))

    return bytes(octets_dechiffres).decode("UTF-8") 

key = 0xCA61
bloc = 0xAB
c = chiffrememnt_bloc(bloc, key)
d = dechiffrement_bloc(c, key)
print(bloc, c, d)
msg="Maram123333"
e=chiff_msg(msg,key)
f=dechiff_msg(e,key)
print(msg,e,f)