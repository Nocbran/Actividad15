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



print("*************MENU RETOS RECURSIVOS***************")
print("1. Invertir una cadena de texto")
print("2. Calcular la suma de los primeros N numeros naturales")
print("3. Imprimir una cuenta regresiva desde N hasta 1")
print("4. Sumar los digitos de un numero")
print("5. Contar cuantos digitos tiene un numero")
print("6. Salir")

opcion = input("Selecciones una opcion: ")
if opcion == "1":
    texto = input("Ingrese el texto que desea invertir: ")
    resultado = Invertir_Cadena(texto)
    print(f"\nEl texto invertido es: {resultado}")
elif opcion == "2":
    numero = int(input("Ingrese un numero positivo "))
    resultadoSuma = Calcular_Suma_N_numero(numero)
    print(f"\nSuma de N numeros es: {resultadoSuma}")
elif opcion == "3":
    Numero = int(input("Ingrese un numero: "))
    print(f"\nCuenta regresiva asta el numero : {Imprimir_Cuenta_Regresiva(Numero)}")