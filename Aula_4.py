"""
    O código pede para o usuário digitar uma palavra e então conta quantas vogais e quantas consoantes essa palavra possui. Para isso, ele percorre cada letra da palavra e verifica se é uma vogal (a, e, i, o, u). Se for, aumenta o contador de vogais; se não for, aumenta o contador de consoantes. Ao final, mostra quantas vogais e consoantes encontrou.

Resumo dos passos:

Recebe a palavra do usuário.
Deixa todas as letras minúsculas e remove espaços extras.
Para cada letra da palavra:
Se for vogal, soma 1 no contador de vogais.
Se não for vogal, soma 1 no contador de consoantes.
Mostra o total de vogais e consoantes.
Observação:
O código considera qualquer letra que não seja vogal como consoante, incluindo números e símbolos, o que pode não ser o ideal.
"""

palavra = input("Qual a palavra deseja contar?").strip().lower()
vogal = 0
consonte = 0

for letra in palavra :
    
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogal += 1
        print(f"{letra} vogal")
    else:
        consonte += 1
        print(f"{letra} consonte")
print("Vogal : ", vogal)
print("Consoante: ", consonte)
