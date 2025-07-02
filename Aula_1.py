
def falando_com_user(): #Criando a função que pede os numeros para a operação
    numero1 = float(input("Digite um numero: ")) #PEDINDO UM NUMERO PARA  O USUÁRIO
    numero2 = float(input("Digite outro numero: ")) # Pedindo outro numero para realizar a operação
    return numero1, numero2

def some(numero1, numero2):# Criando a função soma e usando as variaveis externas
    resultado_soma = numero1 + numero2 # Criando o resultado da soma
    print(resultado_soma)# Está exibindo o resultado da soma
    return 

def subtracao(numero1, numero2):# Criando a função da subtração e usando variaveis externas
    resultado_subtracao = numero1 - numero2 # Criando o resultado da subtração
    print(resultado_subtracao)# Exibindo o resultado da operação realizada
    return

def multiplicacao(numero1, numero2):# Criando a função da multiplicação e usando variaveis externas
    resultado_multiplicacao = numero1 * numero2 # Criando o resultado da multiplicação
    print(resultado_multiplicacao)# Exibindo o resultado da multiplicação
    return

def divisao(numero1, numero2):# Criando a função da divisao e usando variaveis externas
    resultado_divisao = numero1 / numero2# Criando o resultado da divisao
    print(resultado_divisao)# Exibindo o resultado da divisão
    return resultado_divisao

def main():# Função principal
    while True:# Manter ele rodando (Loop)

        print("===== Bem vindo ao app da calculadora")# Inicio do programa 
        a, b = falando_com_user()# As variaveis dentro da função estão sendo armazenadas dentro das variaveis A e B
        print("Escolha a operação: ") #Exibir para o user
        print("Somar = 1") #Exibir para o user
        print("Subtracao = 2") #Exibir para o user
        print("multiplicacao = 3") #Exibir para o user
        print("divisao = 4") #Exibir para o user
    
        operacao = int(input("Qual a operação que vc quer fazer: "))# Criando a variavel que coleta as opções oferecidas ao usuário 

        if operacao == 1: # Se a operção for igual a 1 
            some(numero1=a,numero2=b)   # Chama a funçao some e dentro dela tem que inserir as variaveis memorizadas da função falando_com_user
        elif operacao == 2: # Se a operção for igual a 1
            subtracao (numero1=a,numero2=b) # Chama a funçao subtração e dentro dela tem que inserir as variaveis memorizadas da função falando_com_user
        elif operacao == 3: # Se a operção for igual a 1
            multiplicacao(numero1=a,numero2=b) # Chama a funçao multipicação e dentro dela tem que inserir as variaveis memorizadas da função falando_com_user
        elif operacao == 4: # Se a operção for igual a 1
            divisao(numero1=a,numero2=b) # Chama a funçao divisão e dentro dela tem que inserir as variaveis memorizadas da função falando_com_user
        break

main()
