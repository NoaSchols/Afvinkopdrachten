print (" We gaan voor 5 dagen insecten vangen en aan het eind optellen")
#De waarden hieronder worden dadelijk overschreven.
dag = 1
insect = 0
#Zolang het 5 of onder de 5 dagen zit gaat hij door
while dag <= 5 :
    insect += int(input("Hoeveel insecten heb je gevangen vandaag? "))
#De insecten per dag worden bij elkaar opgeteld

    dag = dag + 1
#En uitgeprint
print ( insect )
    
    



