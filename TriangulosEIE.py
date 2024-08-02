def obtener_lados():
    while True:
        try:
            a = float(input("INGRESE EL LADO A DEL TRIANGULO: "))
            b = float(input("INGRESE EL LADO B DEL TRIANGULO: "))
            c = float(input("INGRESE EL LADO C DEL TRIANGULO: "))

            if a <= 0 or b <= 0 or c <= 0:
                print("Los lados deben ser números positivos. Inténtelo de nuevo.")
                continue

            # Verificación de la desigualdad triangular
            if a + b > c and a + c > b and b + c > a:
                return a, b, c
            else:
                print("Los valores ingresados no forman un triángulo válido. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")


def determinar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "EL TRIANGULO ES EQUILATERO"
    elif a == b or a == c or b == c:
        return "EL TRIANGULO ES ISOSCELES"
    else:
        return "EL TRIANGULO ES ESCALENO"


def main():
    print("Bienvenido al verificador de triángulos.")
    a, b, c = obtener_lados()
    tipo_triangulo = determinar_tipo_triangulo(a, b, c)
    print(tipo_triangulo)


if __name__ == "__main__":
    main()
