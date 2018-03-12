print("Herzlich willkmen zum Taschenrechner")
live = "false"
while(live == "false"):
    zahl1 = int(input("Bitte geben Sie einen  Zahl ein"))
    zahl2 = int(input("Bitten geben Sie noch eine Zahl ein"))
    funktion = input("Bitte funktion wählen")
    if(funktion == "+"):
        summe = zahl1 + zahl2
    if(funktion == "-"):
        summe = zahl1 - zahl2
    if(zahl1 != 0):
        if(zahl2 != 0):
            if(funktion == ":"):
                summe = zahl1/zahl2
        elif(zahl2 == 0):
            summe = "ungültig"

        
    elif(zahl1 == 0):
        summe = "ungültig"
    if(funktion == "*"):
        summe = zahl1*zahl2
    print(summe)
    live12 = input("Taschenrechner abrechen")
    if(live12 == "ja"):
        live == "true"
    if(live12 == "nein"):
        live = "false"
