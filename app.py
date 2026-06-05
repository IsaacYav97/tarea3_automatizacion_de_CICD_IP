import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo.")
    return math.sqrt(a)

def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero.")
    return a % b

def logaritmo(a):
    if a <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos.")
    return math.log10(a)

historial = []

def mostrar_historial():
    if not historial:
        print("\nNo hay operaciones en el historial.")
    else:
        print("\n=== Historial ===")
        for i, entrada in enumerate(historial, 1):
            print(f"  {i}. {entrada}")

def calculadora():
    print("╔══════════════════════════════╗")
    print("║      CALCULADORA AVANZADA    ║")
    print("╚══════════════════════════════╝")

    menu = """
Operaciones disponibles:
  1. Sumar
  2. Restar
  3. Multiplicar
  4. Dividir
  5. Potencia
  6. Raíz cuadrada
  7. Módulo (resto)
  8. Logaritmo base 10
  9. Ver historial
  0. Salir
"""

    while True:
        print(menu)
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("\nHasta luego!")
            break

        elif opcion == "9":
            mostrar_historial()
            continue

        elif opcion == "6" or opcion == "8":
            try:
                a = float(input("Ingresa el número: "))
                if opcion == "6":
                    resultado = raiz_cuadrada(a)
                    entrada = f"√{a} = {resultado:.4f}"
                else:
                    resultado = logaritmo(a)
                    entrada = f"log10({a}) = {resultado:.4f}"
                print(f"\n  Resultado: {resultado:.4f}")
                historial.append(entrada)
            except ValueError as e:
                print(f"\n  Error: {e}")

        elif opcion in ["1", "2", "3", "4", "5", "7"]:
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))

                if opcion == "1":
                    resultado = sumar(a, b)
                    simbolo = "+"
                elif opcion == "2":
                    resultado = restar(a, b)
                    simbolo = "-"
                elif opcion == "3":
                    resultado = multiplicar(a, b)
                    simbolo = "×"
                elif opcion == "4":
                    resultado = dividir(a, b)
                    simbolo = "÷"
                elif opcion == "5":
                    resultado = potencia(a, b)
                    simbolo = "^"
                elif opcion == "7":
                    resultado = modulo(a, b)
                    simbolo = "%"

                print(f"\n  Resultado: {a} {simbolo} {b} = {resultado:.4f}")
                historial.append(f"{a} {simbolo} {b} = {resultado:.4f}")

            except ValueError as e:
                print(f"\n  Error: {e}")

        else:
            print("\n  Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    calculadora()