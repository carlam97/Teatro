from rich import print
import math

caixa = 0

print("-="*60)
print("PROJETO TEATRO EM PYTHON")
print("-="*60)
print("Sessão de teatro!")

l = int(input("Quantidade de linhas: "))
c = int(input("Quantidade de colunas: "))

preco_cadeira = 100

matriz_teatro = []
for i in range(l):
    matriz_fileira = []
    for j in range(c):
        matriz_fileira.append("L")
    matriz_teatro.append(matriz_fileira)
    
print(matriz_teatro)
print()

while True:
    print("O preço para venda de cada cadeira é de R$100,00")
    print()
    
    print("Qual acento o(a) senhor(a) deseja? ")
    
    fileira = int(input("Fileira: ")) -1
    coluna = int(input("Coluna: ")) -1
    
    erro = fileira > l or coluna > c   
    if erro:
        input("ERRO")
    else: 
        if matriz_teatro[fileira][coluna] == "L": 
            
            cond = input("Esta cadeira está LIBERADA, deseja ALUGAR ou COMPRAR?")
            if cond == "comprar":
                caixa += preco_cadeira
                matriz_teatro[fileira][coluna] = "V"
            elif cond == "alugar":
                caixa += preco_cadeira * 0.3
                matriz_teatro[fileira][coluna] = "A"
                
        elif matriz_teatro[fileira][coluna] == "V":
            print("Está cadeira não está disponível para compra")
        
        elif matriz_teatro[fileira][coluna] == "A":
            print("Está cadeira já está alugada!")
            print("Neste caso você pagará apenas 70% do valor total da cadeira (R$70,00)")
            cond = input("Deseja comprá-la?? Sim / Não" )
            if cond == "sim":
                caixa += preco_cadeira * 0.7
                matriz_teatro[fileira][coluna] = "V"
                
    sair = input("Deseja continuar? -- sim / nao: ")
    
    if sair == "nao":
        cont = 0
        for i in range(l):
            for j in range(c):
                if(matriz_teatro[i][j] != "L"):
                    cont += 1
            
        qtd_min = math.floor((l*c)/2) + 1   
            
        if cont >= qtd_min:
            break    
            
            
        input("Não é possível fechar o teatro agora. Você não atingiu 50% + 1 das cadeiras vendidas/alugadas")    
        
        
print(matriz_teatro)
print(caixa)