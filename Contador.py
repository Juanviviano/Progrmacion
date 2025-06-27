# contador.py

def es_par_o_impar(numero):
    """Devuelve si el número es 'par' o 'impar'."""
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def cuenta_regresiva(n):
    """Función recursiva que imprime los números desde n hasta 0 con su paridad."""
    if n < 0:
        return
    print(f"{n} - {es_par_o_impar(n)}")
    cuenta_regresiva(n - 1)
