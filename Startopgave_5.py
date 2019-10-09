# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je 
# die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein 
# proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de 
# tijd.

  
    
def lees_inhoud(bestands_naam):
    """Schrijf hier je eigen code die het fasta bestand inleest en deze 
    splitst in headers en sequenties.
    Lever twee strings:
        - header = string, header van fasta
        - seq = string met daarin de sequentie behorend bij de header
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
    bestand = open(bestands_naam)
    header = ""]
    seq = ""
    
    return header, seq

    
def is_dna(seq):
    """Deze functie bepaalt of de sequentie (een element uit seqs)
    DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    

def knipt(seq):
    """Bij deze functie kan je een deel van de code die je de afgelopen 
    2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie 
    (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je 
    alleen maar printjes maken.
    """

def main():
    # Voer hier de bestandsnaam van het juiste bestand in, of hernoem 
    # je bestand
    bestand = "alpaca.fa" 
    # Hier onder vind je de aanroep van de lees_inhoud functie, 
    # die gebruikt maakt van de bestand variabele als argument. 
    # De resultaten van de functie, de lijst met headers en de lijst 
    # met sequenties, sla je op deze manier op in twee losse resultaten.
    headers, seqs = lees_inhoud(bestand) 
        
    zoekwoord = input("Geef een zoekwoord op: ")

    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
main()
