print("Digite 2 valores")

val_1 = float(input("Digite o 1º valor "))
val_2 = float    (input("Digite o 2º valor "))

# print("A soma é", val_1 + val_2)
# print("A subtração é", val_1 - val_2)
# print("A divisão é", val_1 / val_2)
# print("A multiplicação é", val_1 * val_2)

operacao = int(input("Digite a operação desejada: 1 = Adição, 2 = Subtração, 3 = Multiplicação, 4 = Divisão "))

if operacao == 1:
    print("A soma é ", val_1 + val_2)
elif operacao == 2:
    print("A subtração é ", val_1 - val_2)
elif operacao == 3:
    print("A multiplicação é ", val_1 * val_2)
elif operacao == 4:
    print("A divisão é ", val_1 / val_2)
else :
    print("Siga as instruções")k