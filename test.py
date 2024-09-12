#binærsøk når vi kan riktig verdi

"""
NB!

DENNE KODEN BRUKER VI IKKE, SE AvstandSjekk.py ISTEDET.

def binary_search(target, low, high):
    while low <= high:
        # Finn midtpunktet
        mid = (low + high) // 2
        print(f"Undersøker midtpunktet: {mid}")

        # Sjekk om vi har funnet målet
        if mid == target:
            print(f"Funnet: {mid}")
            return mid

        # Hvis målet er mindre enn midtpunktet, juster high
        elif mid > target:
            print(f"{target} er mindre enn {mid}, går ned.")
            high = mid - 1

        # Hvis målet er større enn midtpunktet, juster low
        else:
            print(f"{target} er større enn {mid}, går opp.")
            low = mid + 1

    print("Tallet ble ikke funnet innenfor intervallet.")
    return None

# Test med tallet 30 i intervallet [1, 100]
binary_search(30, 1, 100)

"""