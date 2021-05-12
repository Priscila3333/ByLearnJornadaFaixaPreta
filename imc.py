altura = float(input('Insira aqui sua altura m:'))
peso = float(input('Insira seu peso kg:'))

imc = peso/altura ** 2

print(f"Seu IMC é: {imc:.4f}")

if imc < 16:
    print("Magreza Grave")

elif imc < 17:
    print("Magreza Moderada")

elif imc < 18.5:
    print("Magreza Leve")

elif imc < 25:
    print("Saudável")

elif imc <30:
    print("Sobrepeso")

elif imc < 35:
    print("Obesidade Grau I")

elif imc < 40:
    print("Obesidade Grau II (Severa)")

else:
    print("Obesidade grau III (Mórbida)")
    
    
