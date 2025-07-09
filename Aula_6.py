salario= float (input("Quanto voce ganha?"))


if salario > 0 and salario <= 400.00:
    salario_reajustado1= salario*0.15
    perc_reajuste1= (salario+salario_reajustado1)
    print(perc_reajuste1)
    print(salario_reajustado1)
    print("15%")

elif salario > 400.01 and salario <= 800.00:
    salario_reajustado1= salario*0.12
    perc_reajuste1= (salario+salario_reajustado1)
    print(perc_reajuste1)
    print(salario_reajustado1)
    print("12%")
    
elif salario >= 800.01 and salario <= 1200.00:
    salario_reajustado1= salario*0.10
    perc_reajuste1= (salario+salario_reajustado1)
    print(perc_reajuste1)
    print(salario_reajustado1)
    print("10%")

elif salario >= 1200.01 and salario <= 2000.00:
    salario_reajustado1=salario*0.07
    perc_reajuste1= (salario+salario_reajustado1)
    print(perc_reajuste1)
    print(salario_reajustado1)
    print("07%")

elif salario > 2000.01:
    salario_reajustado1= salario*0.04
    perc_reajuste1= (salario+salario_reajustado1)
    print(perc_reajuste1)
    print(salario_reajustado1)
    print("04%")

