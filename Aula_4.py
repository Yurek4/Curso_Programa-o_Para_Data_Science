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
