# Fórmula de Bhaskara
import math


math.sqrt

print("Vamos calular Bhaskare")
A = float(input("Digite o valor de A "))
B = float(input("Digite o valode de B "))
C = float(input("Digite o valode de C "))

#Calc de delta
delta = ((B**2) - 4*A*C)

r1 = - B + math.sqrt(delta)/2*A
r2 = - B - math.sqrt(delta)/2*A