def encontrar_k_esima_contrasena(K, cuadrilla1, cuadrilla2):
    from itertools import product
    
    columnas1 = [''.join([fila[i] for fila in cuadrilla1]) for i in range(5)]
    columnas2 = [''.join([fila[i] for fila in cuadrilla2]) for i in range(5)]
    
    combinaciones = list(product(*[
        sorted(set(columnas1[i]) & set(columnas2[i])) 
        for i in range(5)
    ]))
    
    if K > len(combinaciones):
        return "NO"
    
    combinaciones.sort()
    return ''.join(combinaciones[K-1])

def main():
    T = int(input())
    resultados = []
    
    for _ in range(T):
        K = int(input())
        cuadrilla1 = [input().strip() for _ in range(6)]
        cuadrilla2 = [input().strip() for _ in range(6)]
        
        resultado = encontrar_k_esima_contrasena(K, cuadrilla1, cuadrilla2)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()




