import random

# Task 1:
cfg = {
    "non_terminals": ["S"],
    "terminals": ["a", "b"],
    "start_symbol": "S",
    "rules": {
        "S": [
            ["a", "S", "b"], # S -> aSb
            [""] # S -> epsilon
        ]
    }
}

def afiseaza_cfg(gramatica):
    print(f"Non-terminale: {gramatica['non_terminals']}")
    print(f"Terminale: {gramatica['terminals']}")
    print(f"Simbol de Start: {gramatica['start_symbol']}")
    print(f"Reguli de Productie: {gramatica['rules']}")

# Task 2:
def genereaza_string_din_cfg(lista_simboluri_curenta, lungime_max):
    # se opreste daca lungime_max este atinsa sau nu mai sunt non-terminale
    idx_nt = -1 # Indexul non-terminalului de inlocuit
    non_terminal_de_inlocuit = None

    # gaseste primul non-terminal (derivatie stanga)
    for i, simbol in enumerate(lista_simboluri_curenta):
        if simbol in cfg["non_terminals"]:
            idx_nt = i
            non_terminal_de_inlocuit = simbol
            break

    # daca nu mai sunt non-terminale sau atingem lungimea maxima pentru terminale ne oprim
    lungime_curenta_terminale = sum(1 for s in lista_simboluri_curenta if s in cfg["terminals"])
    if non_terminal_de_inlocuit is None or lungime_curenta_terminale >= lungime_max:
        return "".join(s for s in lista_simboluri_curenta if s in cfg["terminals"])

    # flip a coin lol
    regula_aleasa = random.choice(cfg["rules"][non_terminal_de_inlocuit])

    # inlocuim non-terminalul cu noua regula
    urmatoarea_lista_simboluri = lista_simboluri_curenta[:idx_nt] + regula_aleasa + lista_simboluri_curenta[idx_nt+1:]

    # ca sa mai scurtam daca e prea lung sirul
    if len(urmatoarea_lista_simboluri) > lungime_max * 2 and [""] in cfg["rules"][non_terminal_de_inlocuit]:
         urmatoarea_lista_simboluri = lista_simboluri_curenta[:idx_nt] + [""] + lista_simboluri_curenta[idx_nt+1:]

    return genereaza_string_din_cfg(urmatoarea_lista_simboluri, lungime_max)


def generator_stringuri(numar_stringuri=10, lungime_maxima=10):
    stringuri_generate = set()
    incercari = 0 # pentru a evita bucle infinite
    while len(stringuri_generate) < numar_stringuri and incercari < numar_stringuri * 5:
        string = genereaza_string_din_cfg([cfg["start_symbol"]], lungime_maxima)
        if len(string) <= lungime_maxima: # verificare finala a lungimii
             stringuri_generate.add(string)
        incercari += 1
    return list(stringuri_generate)

# Task 3:
def afiseaza_derivare(string_tinta):
    # afiseaza o derivatie stanga pentru un string tinta daca apartine limbajului a^n b^n
    print(f"Incercare derivare pentru: '{string_tinta if string_tinta else 'ε'}'")

    # trebuie sa fie a^n b^n
    n = 0
    structura_valida = True
    if not string_tinta: # Cazul epsilon
        print(f"{cfg['start_symbol']} -> ε")
        return

    # a count
    while n < len(string_tinta) and string_tinta[n] == 'a':
        n += 1

    # verifica daca restul sunt 'b'-uri si daca numarul corespunde
    for i in range(n):
        if (n + i >= len(string_tinta)) or (string_tinta[n + i] != 'b'):
            structura_valida = False
            break
    if len(string_tinta) != 2 * n: # asigura consumarea tuturor caracterelor
        structura_valida = False

    if not structura_valida:
        print(f"String-ul '{string_tinta}' nu respecta structura a^n b^n sau nu este in limbaj.")
        return

    # realizeaza derivarea
    derivare_curenta = cfg['start_symbol']
    print(derivare_curenta, end="")

    for _ in range(n): # Aplica S -> aSb de n ori
        parti = derivare_curenta.split(cfg['start_symbol'], 1)
        derivare_curenta = parti[0] + "a" + cfg['start_symbol'] + "b" + parti[1]
        print(f" -> {derivare_curenta}", end="")

    parti = derivare_curenta.split(cfg['start_symbol'], 1)
    derivare_curenta = parti[0] + "" + parti[1] # Inlocuire cu epsilon
    print(f" -> {derivare_curenta if derivare_curenta else 'ε'}")


# Task 4:
def testeaza_apartenenta(string_intrare, lungime_max=12):
    # verifica daca un string dat apartine limbajului definit de CFG (a^n b^n)
    if len(string_intrare) > lungime_max:
        #print(f"String-ul '{string_intrare}' depaseste lungimea maxima de {lungime_max}.") #Comentat pentru a reduce output-ul
        return False

    if not string_intrare: # string vid (ε)
        return True # S -> ε

    # verifica daca lungimea este para
    if len(string_intrare) % 2 != 0:
        return False

    n = len(string_intrare) // 2

    # verifica daca primele n caractere sunt 'a'
    for i in range(n):
        if string_intrare[i] != 'a':
            return False

    # verifica daca urmatoarele n caractere sunt 'b'
    for i in range(n):
        if string_intrare[n + i] != 'b':
            return False
    return True

def main():
    print("Definitia CFG-ului:")
    afiseaza_cfg(cfg)
    print("\nGenerator de String-uri:")
    stringuri_generate_main = generator_stringuri(numar_stringuri=5, lungime_maxima=6) # redus numarul pentru concizie
    print(f"String-uri generate:")
    for s_main in stringuri_generate_main:
        print(s_main if s_main else "ε")

    print("\nDerivare:")
    stringuri_pentru_derivare = ["aabb", "ab", "", "aab"] # set redus
    for s_main in stringuri_pentru_derivare:
        afiseaza_derivare(s_main)
        print()

    print("\nTestare Apartenenta:")
    stringuri_de_testat = ["aabb", "ab", "", "aab", "bba", "aaabbb", "aaaaabbbbba"] # set redus
    for s_main in stringuri_de_testat:
        este_membru = testeaza_apartenenta(s_main)
        print(f"String-ul '{s_main if s_main else 'ε'}' este membru? {este_membru}")

if __name__ == "__main__":
    main()