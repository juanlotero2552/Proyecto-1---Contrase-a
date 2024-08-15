import itertools

def encontrar_k_esima_contrasena(K, cuadrilla1, cuadrilla2):
    columnas1 = [''.join(fila[i] for fila in cuadrilla1) for i in range(5)]
    columnas2 = [''.join(fila[i] for fila in cuadrilla2) for i in range(5)]

    print("Columnas 1:", columnas1)
    print("Columnas 2:", columnas2)

    contraseñas_posibles = itertools.product(columnas1[0], columnas1[1], columnas1[2], columnas1[3], columnas1[4])
    contraseñas_posibles = sorted(set(''.join(c) for c in contraseñas_posibles))

    print(f"Número de contraseñas posibles: {len(contraseñas_posibles)}")

    if 1 <= K <= len(contraseñas_posibles):
        return contraseñas_posibles[K-1]
    else:
        return "NO"

def main():
    import sys
    input = sys.stdin.read
    datos = input().splitlines()

    print("Datos leídos:", datos)

    indice = 0
    T = int(datos[indice])
    indice += 1

    resultados = []
    for _ in range(T):
        K = int(datos[indice])
        indice += 1

        cuadrilla1 = [datos[indice + i] for i in range(6)]
        indice += 6
        cuadrilla2 = [datos[indice + i] for i in range(6)]
        indice += 6

        print("Cuadrilla 1:", cuadrilla1)
        print("Cuadrilla 2:", cuadrilla2)
        print(f"K: {K}")

        resultado = encontrar_k_esima_contrasena(K, cuadrilla1, cuadrilla2)
        resultados.append(resultado)

    print("Resultados:", resultados)

    with open("salida.txt", "w") as f:
        for resultado in resultados:
            f.write(resultado + "\n")

if __name__ == "__main__":
    main()



