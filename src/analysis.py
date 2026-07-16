import spn_core

def nb_difference(a,b):
    return bin(a^b).count('1')

def test_effet_avalanche(key):
    totaux = [0, 0, 0, 0]
    nb_tests = 0
    for bloc_original in range(256):
        for bit in range(8):
            bloc_modifie=bloc_original^(1<<bit)
            resultats_original=spn_core.chiffrer_bloc_par_round(bloc_original,key)
            resultats_modifie=spn_core.chiffrer_bloc_par_round(bloc_modifie,key)
            for round_num in range(4):
                diff=nb_difference(resultats_original[round_num],resultats_modifie[round_num])
                totaux[round_num]=totaux[round_num]+diff
            nb_tests+=1
    for round_num in range(4):
        moyenne=totaux[round_num]/nb_tests
        pourcentage=(moyenne/8)*100
        print(f"Round {round_num +1}: {moyenne:.2f} bits en moyenne ({pourcentage: .1f}%)")
test_effet_avalanche(0xCA61)