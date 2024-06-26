import matplotlib.pyplot as plt

#sparbuch = []
#EK = 0
#def spar_funktion(AK, SR, i, lz, EK):
#    AK1 = AK*(1+0.01)
#    for lz in range (1, lz+1):
#        EK += (AK1+SR)*(1+i)**lz
#        sparbuch.append(EK)
#    print(sparbuch)
        
#spar_funktion(10000, 1000, 0.01, 10, 0)
#Problem: ak1 ist bereits einmal verzinst

#EK = 0
#def spar_funktion(AK, SR, i, lz, EK):
#    AK1 = AK*(1+i)
#    for lz in range (1, lz+1):
#        EK += (AK1+SR)*(1+i)**lz
#        sparbuch.append(EK)
#    print(sparbuch)


#--folgendes ist vom Prof--
def spar_funktiona(AK, SR, r, lz):
    kapital = AK
    gesamt_kapital = []
    
    for k in range (1, lz+1):
        kapital = SR + kapital * (1+r)
        gesamt_kapital.append(kapital)
        
    return gesamt_kapital

end_kapital = spar_funktiona(10000, 1000, 0.01, 10)

plt.bar(range(1,11), end_kapital)