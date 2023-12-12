import numpy as np

class MatrizAdjacencia:
    def __init__(self):
        self.matriz_adj = {
            "MatrizSorteada": np.array([
                [0,1,1,0,1,1,0,0,0,1], # 1 site que faz referencia
                [0,0,1,0,0,0,0,0,0,0], # 2 site que faz referencia
                [0,0,0,0,0,0,0,0,0,1], # 3 site que faz referencia
                [0,1,1,0,0,1,1,0,0,1], # 4 site que faz referencia
                [0,0,0,1,0,0,0,0,0,0], # 5 site que faz referencia
                [0,1,0,0,0,0,0,0,0,0], # 6 site que faz referencia
                [0,0,0,0,0,0,0,0,1,0], # 7 site que faz referencia
                [0,0,0,0,0,1,0,0,0,0], # 8 site que faz referencia
                [0,1,1,0,0,1,0,1,0,1], # 9 site que faz referencia
                [0,0,0,0,0,1,0,0,0,0], # 10 site que faz referencia

                #[0,0,1,0],
                #[1,0,0,0],
                #[1,1,0,0],
                #[0,1,0,0],
            ]) 
    }
 

    def Autoridadecalculo(self):
        for i, matriz in self.matriz_adj.items():
            self.calcular_autoridade(matriz)
            print()

    def calcular_autoridade(self, matriz):
        calculo = CalcularRank()
        vetor = calculo.calcular_vetor_autoridade(matriz, 1000, 0.00001)
        vetor_ordenados = calculo.ordenar(vetor)
        print("Vetor de autoridade para a matriz 10x10:")
        
        for valores in vetor_ordenados:
            print(f"Site {valores[0]}: {valores[1]:.5f}")

class CalcularRank:
    def calcular_vetor_autoridade(self, A, iteracoes, tolerancia):
        a0 = self.somas_colunas_normalizadas(A)

        for _ in range(iteracoes):
            Av = np.dot(A, a0)
            AtAv = np.dot(np.transpose(A), Av)
            a1 = self.normalizar(AtAv)

            if np.linalg.norm(np.subtract(a1, a0)) < tolerancia:
                break

            a0 = a1

        return a0.tolist()

    def somas_colunas_normalizadas(self, A):
        colunas_soma = np.sum(A, axis=0)
        return self.normalizar(colunas_soma)

    def normalizar(self, v):
        norma = np.linalg.norm(v)
        return v / norma if norma != 0 else v

    def ordenar(self, vetor):
        return sorted(enumerate(vetor, start=1), key=lambda x: x[1], reverse=True)

class Principal():
    principal = MatrizAdjacencia()
    principal.Autoridadecalculo()