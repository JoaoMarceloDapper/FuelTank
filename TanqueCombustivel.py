tanque = 500

while tanque > 0:
    print("litros disponiveis:", tanque)
    abastecida = int(input("litros abastecidos: "))
    if tanque -  abastecida >=0:
        tanque = tanque - abastecida
    else :
        print("nao temos litros disponiveis")
print("o que sobrou do tanque foi", tanque)
print("volte sempre!")