horas_de_viagem= int(input("Jõao, quanto tempo voce gastou na sua viagem? "))
velo_med = int(input("Qual foi a velocidade média? "))

# Distância = Velocidade Média * Tempo Gasto. 
def calc_distancia():
    distancia = velo_med * horas_de_viagem
    return distancia

def calc_litros():
    litros= recebe_distancia/ 12 
    
    return litros

recebe_distancia = calc_distancia()
recebe_litros = calc_litros()
print(f"A quantidade de litros que vai ser usada é {recebe_litros:.3f}" )
