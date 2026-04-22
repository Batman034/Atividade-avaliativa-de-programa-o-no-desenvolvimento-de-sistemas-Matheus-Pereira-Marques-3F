import os
os.system('cls')

while True:
        idade = int(input("Digite sua idade: "))

        if idade < 16:
                print("Não pode votar.")

        elif idade >= 16 and idade < 18:
                print("Você pode votar *por opção*.")

        elif idade == 18:
                print("Você é obrigado a votar.")

        elif idade > 18 and idade < 70:
                print("Você é obrigado a votar.")

        elif idade == 70:
                print("Você é obrigado a votar.")
                
        elif idade > 70:
                print("Você pode votar *por opção*.")
