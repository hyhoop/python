from colorama import init,Fore
init()
def cual_es_la_grande(elemento1,elemento2,elemento3):
    elemento11 = len(elemento1)
    elemento22 = len(elemento2)
    elemento33 = len(elemento3)

    if elemento11 > elemento22 and elemento11 > elemento33:
        return elemento1
    elif elemento22 > elemento11 and elemento22 > elemento33:
        return elemento2
    elif elemento33 > elemento11 and elemento33 > elemento22:
        return elemento3

def main():
    titulo = "¿Cual es la palabra mas larga?"
    print(titulo + "\n" + "-" * len(titulo))

    palabra1 = input("Ingresa una palabra: ")
    palabra2 = input("Ingresa una palabra: ")
    palabra3 = input("Ingresa una palabra: ")
    numero = cual_es_la_grande(palabra1,palabra2,palabra3)
    print("La palabra más grande es: {}".format(Fore.BLUE + numero + Fore.RESET))

if __name__ == "__main__":
    main()