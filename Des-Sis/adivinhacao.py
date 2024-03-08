import random 
print("Dificuldade\n-Baby(B)- Tentativas Infinitas\n--Easy(E) 5 Tentativas\n---Medium(M) 5 Tentativas\n----Hard(H) 3 Tentativas\n-----God(G) 2 Tentativas")

level = input("")

if (level == "B"):
    sorteio = random.randint (1,5)
    t= 9999
    print("Os números vão de: 1-5")
elif (level == "E"):
    sorteio = random.randint (1,10)
    t=5
    print("Os números vão de: 1-10")
elif (level == "M"):
    sorteio = random.randint (1,50)
    t=5
    print("Os números vão de: 1-50")
elif (level == "H"):
    sorteio = random.randint (1,200)
    t=3
    print("Os números vão de: 1-200")
elif (level == "G"):
    sorteio = random.randint (1,999)
    t=2
    print("Os números vão de: 1-999")
print("\nAdivinhe o número ")


while (t >= 1):
    chute = int(input("Digite o valor do seu chute: \n"))
    acertou = chute == sorteio
    maior   = chute > sorteio
    menor   = chute < sorteio

    if (acertou) :
        print("Você acertou! \n END GAME")
        break
    elif (chute == 13):
        print("Faz o L")
    elif (maior):
        print("***O número que você digitou é maior***\n")
    elif (menor):
        print("***O número que você digitou é menor***\n")
    t= t -1
    print("---Tentavivas restantes:---", t)
    if (t == 0):
        print("Perdeu otário")
        print("O número era:", sorteio)