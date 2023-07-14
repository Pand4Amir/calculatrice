while True :
    premierResultat = input ("choisis un nbr :")


    print ("[1]:+")
    print ("[2]:-")
    print ("[3]:/")
    print ("[4]:*")

    userInputSymbole = input ("choisis un symbole d'opération :")
    deuxiemeResultat = input ("choisis un nbr :")

    if int (userInputSymbole) == 1:
        print ("addition")
        print (int (premierResultat) + int (deuxiemeResultat))
    elif int (userInputSymbole) == 2:
        print ("soustraction")
        print (int (premierResultat) - int (deuxiemeResultat))
    elif int (userInputSymbole) == 3 :
        print ("division")
        print (int (premierResultat) / int (deuxiemeResultat))
    elif int (userInputSymbole) == 4 :
        print ("multiplication")
        print (int (premierResultat) * int (deuxiemeResultat))
    else : 
        print ("ton operation n'éxiste pas")
