permut=[6,4,7,5,2,0,1,3]
assert(len(permut)==8),"la taille de permut est differente de 8 "
def permuter(bloc):
    bin_str = format(bloc, '08b')
    ch=["0"]*8
    for i in range(8):
       ch[permut[i]] = bin_str[i]
    return(int("".join(ch),2))


def inv_permuter(bloc):
    bin_str=format(bloc,'08b')
    ch=["0"]*8
    for i in range(8):
       ch[i] = bin_str[permut[i]]
    return(int("".join(ch),2))
