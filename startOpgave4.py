# Iteratie opdracht
# Start script voor opgave over sikkelcel
# (c) Martijn van der Bruggen, 2007-2010
# Updates:
# November 2010, code bijgewerkt met instructies voor de opdracht
# Hogeschool van Arnhem en Nijmegen

# Sequenties voor respectievelijk sikkelcel- en normale cellen
# Bekend is dat het gen coderend voor hemoglobine bij sikkelcel aandoening een andere nucleotide heeft
# De sequentie voor de sikkelcel en een "gezonde bloedcel" zijn hier onder gegeven
sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

# In het bestand enzymen.txt staan kandidaat restrictie enzymen
# Opdracht schrijf een programma dat al deze enzymen doorloopt een suggestie
# geeft welk restrictie enzym welk knipt in de ene sequentie en niet in de andere sequentie
# Hiermee kunnen we diagnostisch enzym voorstellen om vast te stellen of een persoon
# drager is van het sikkelcel allel
##We gaan het bestand openen
bestand = open ("enzymen.txt")
##We maken een loop zodat elke regel gelezen wordt 
for i in bestand:

    regel = bestand.readline()
    
    enzym, seq = regel.split()
    
    seq = seq.replace("^","")
##Als het enzym voorkomt in het sikkelenzym print hij YES, ander no.
    if seq in sikkel_seq :
        print ("YES!")
    else :
        print ("No")
##Nu kijken we of het enzym in allebei voorkomen of dat hij verschillend voorkomt.
    if seq in normaal_seq and seq in sikkel_seq:
        print ("Ze knippen allebei!")
    elif seq in normaal_seq and not seq in sikkel_seq:
        print ("Hij knipt in de normaal_seq")
    elif seq in sikkel_seq and not seq in normaal_seq:
        print ("Hij knipt in de sikkel_seq")
    else:
        print ("Hij knipt nergens")

##Dat is het einde van mijn gedeelte van het script.






# Aanwijzingen voor het schrijven van je programma
# -------------------------------------------------------------
# Het lezen van een regel kan met bestand.readline()
# Lees door totdat je een lege regel aantreft
# Een regel bestaat uit twee stukken enzym en knipsequentie. Bijvoorbeeld: DdeI C^TGAG
# Het opsplitsen van een regel in twee stukken op de spatie kan middels: enzym, seq = regel.split()
# Door bovenstaande split verkrijg je twee variabelen enzym en seq, respectievelijk de naam van het enzym en de sequentie waar deze in knipt
# Verwijderen het dakje uit de seq met seq.replace
#   Startcode_Afvinkopdracht4
# Auteur: Noa Schols
# Datum: 2-10-2019
# Functie: kijken welke enzymen er wel en niet in bepaalde genoomsequenties zit.


