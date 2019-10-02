#De waarden hieronder wordt overschreven.
rondje = 0

print (" We gaan rondjes rennen! ")
#De range gaat van 1 tot en met 5, je kan 5 rondjes rennen.
for rondje in range(1,6):
    rondje += rondje
    int(input("Hoeveel seconde duurde je rondje" ))

#Hij print de totaalaantal rondjes, de kortste,langste en de gemiddelde tijd.
print (rondje)
kortste = int(input(" Hoeveel seconde duurde je kortste ronde? "))
langste = int(input(" Hoeveel seconde duurde je langste ronde? "))
gemiddelde = rondje/6

print (kortste)
print (langste)
print (gemiddelde)
#Eind van het script.





        


