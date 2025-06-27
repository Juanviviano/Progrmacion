# main.py

import contador

def main():
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        if numero >= 0:
            contador.cuenta_regresiva(numero)
        else:
            print("Por favor, ingresa un número mayor o igual a 0.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número entero.")

if __name__ == "__main__":
    main()
