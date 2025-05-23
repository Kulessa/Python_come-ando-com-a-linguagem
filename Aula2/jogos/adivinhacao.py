print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = 42
chute_texto = input("Digite o seu numero: ")
print("Você digitou: ", chute_texto)
chute_inteiro = int(chute_texto)
if (chute_inteiro == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo")
