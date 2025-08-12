def Invertir_Cadena(palabra):
    if len(palabra) <= 1:
        return palabra
    else:
        return Invertir_Cadena(palabra[1:]) + Invertir_Cadena(palabra[0])

def Calcular_Suma_N_numero(n):
    if n == 1:
        return n
    else:
        return n + Calcular_Suma_N_numero(n-1)

def Imprimir_Cuenta_Regresiva(n):
    print(f"Cuenta regresiva: {n}")
    if n == 1:
        return  n
    else:
        return Imprimir_Cuenta_Regresiva(n-1)



def MostrarMenu():
    print("\n"+"*"*45)
    print("______________MENÚ PRINCIPAL______________")
    print("*"*45)
    print("1. Invertir una cadena de texto")
    print("2. Calcular la suma de los primeros N numeros naturales")
    print("3. Imprimir una cuenta regresiva desde N hasta 1")
    print("4. Sumar los digitos de un numero")
    print("5. Contar cuantos digitos tiene un numero")
    print("6. Salir")
    print("_"*25)

def opcion_invertir():
    print("\n*** Invertir Cadena ***")
    texto = input("Ingrese el texto (o escriba 'menu' para regresar): ")
    if texto.lower() == "menu":
        return
    print(f"Texto invertido: {Invertir_Cadena(texto)}")

def opcion_sumar_n():
        print("\n*** Suma de N Números Naturales ***")
        while True:
            entrada = input("Ingrese un número positivo (o 'menu' para regresar): ")
            if entrada.lower() == "menu":
                return
            if entrada.isdigit() and int(entrada) > 0:
                numero = int(entrada)
                print(f"Suma total: {Calcular_Suma_N_numero(numero)}")
                break
            else:
                print("Numero invalido, intentelo de nuevo.")

def opcion_cuenta_regresiva():
        print("\n*** Cuenta Regresiva ***")
        while True:
            entrada = input("Ingrese un número positivo (o 'menu' para regresar): ")
            if entrada.lower() == "menu":
                return
            if entrada.isdigit() and int(entrada) > 0:
                numero = int(entrada)
                print(f"Cuenta regresiva:{Imprimir_Cuenta_Regresiva(numero)} ")
                break
            else:
                print("Numero invalido, intentelo de nuevo.")

def main():
    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_invertir()
        elif opcion == "2":
            opcion_sumar_n()
        elif opcion == "3":
            opcion_cuenta_regresiva()
        elif opcion == "4":
            continue
        elif opcion == "5":
            continue
        elif opcion == "6":
            print("\n Hasta pronto!")
            break
        else:
            print("Opción inválida, intente de nuevo.")
main()