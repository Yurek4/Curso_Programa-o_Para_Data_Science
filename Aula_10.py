primeiro_num = float(input("Digite um valor: "))
inicial = primeiro_num

notas = [100,50,20,10,5,2]
moedas = [1, 0.50, 0.25,0.10,0.05,0.01]

print("NOTAS")
for i in notas:
    quantidade_notas = primeiro_num//i
    primeiro_num = primeiro_num-(quantidade_notas*i)
    print(f"total de notas para valor {i} é {quantidade_notas} ")

print("MOEDAS")
for e in moedas:
    quantidade_moedas = primeiro_num//e
    primeiro_num = primeiro_num-(quantidade_moedas*e)
    print(f"total de notas para valor {e} é {quantidade_moedas} ")
    

