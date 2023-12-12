import numpy as np #Importa a biblioteca NumPy

def conveniente(matriz):#Calcula autovalor e autovetor
    autovalores, autovetores = np.linalg.eig(matriz)
    return autovalores, autovetores

def obterMatrizUsuario(dimensao):#Vê o tamanho da matriz
    print(f"Digite os elementos da matriz {dimensao}x{dimensao} (separados por espaços):")
    matriz = np.zeros((dimensao, dimensao))
    for i in range(dimensao):
        linha = input(f"Linha {i + 1}: ").split()
        matriz[i] = [float(x) for x in linha]
    return matriz

tamanhoMatriz = int(input("Digite o tamanho da matriz (2 a 10): "))

tamanhoMatriz = max(2, min(tamanhoMatriz, 10))

matrizUsuario = obterMatrizUsuario(tamanhoMatriz)

autovalores, autovetores = conveniente(matrizUsuario)

print("\nMatriz inserida pelo usuário:")
print(matrizUsuario)
print("\nAutovalores:")
print(autovalores)
print("\nAutovetores:")
print(autovetores)