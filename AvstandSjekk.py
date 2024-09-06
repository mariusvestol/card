#poenget med denne koden er at armen skal finne nærmeste punkt der kortet aktiveres
#dette gjør den ved å gradvis sjekke når kortet aktiveres og ikke
#og deretter øker/minker avstanden til terminalen. dette vil ende med at armen hopper mellom to verdier
# og den vil da ha funnet maksimal avstand til terminalen for at kortet skal aktiveres


#if(avstand == morendin):
#	print("feit")

#binærsøk når vi kan riktig verdi

def check_connection(distance):
    """
    Simulerer sjekk om terminalen har forbindelse på en gitt avstand.
    Denne funksjonen skal erstattes med den faktiske implementasjonen
    som sjekker tilkoblingen og returnerer en boolean-verdi.
    """
    # Eksempel: Her simulerer vi at forbindelsen er stabil opp til 75 cm
    max_stable_distance = 75
    return distance <= max_stable_distance  # True hvis innenfor grensen

def find_max_distance(low, high):
    """
    Funksjon for å finne maksimal avstand der forbindelsen er stabil
    ved bruk av en binærsøkalgoritme.
    """
    best_distance = low  # Start med minimumsavstanden som et gyldig alternativ

    while low <= high:
        # Finn midtpunktet
        mid = (low + high) // 2
        print(f"Tester avstand: {mid} cm")

        # Bruk check_connection for å sjekke om terminalen har forbindelse
        if check_connection(mid):
            print(f"Tilkobling OK på {mid} cm, prøver lengre avstand.")
            best_distance = mid  # Oppdater beste avstand til midtpunktet
            low = mid + 1        # Juster for å søke i den øvre halvdelen
        else:
            print(f"Ingen tilkobling på {mid} cm, prøver kortere avstand.")
            high = mid - 1       # Juster for å søke i den nedre halvdelen

    print(f"Maksimal stabil avstand funnet: {best_distance} cm")
    return best_distance

# Eksempel: Sett et interval for søket, f.eks. 0 til 100 cm
find_max_distance(0, 100)
