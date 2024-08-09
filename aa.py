idade = int(input("Digite uma idade:"))

if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")