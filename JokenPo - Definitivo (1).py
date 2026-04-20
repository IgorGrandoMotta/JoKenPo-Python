import random
pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papel = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

pj1 = 0
pj2 = 0
pmqn = 0
pmqn1 = 0
pmqn2 = 0
empatesjj = 0
empatesjm = 0
empatesmm = 0
 

print("--- Modos de jogo ---")
print("(1) Humano x Humano")
print("(2) Humano x Máquina")
print("(3) Máquina x Máquina")
print("(4) Sair")
print("---------------------")
modojogo = int(input("Selecione modo de jogo: "))

while True:
    # ─────────────────────────────────────────────
    # MODO 1 — Humano x Humano
    # ─────────────────────────────────────────────
    if modojogo == 1:
        print("\n","------- REGRAS -------")
        print("Para Pedra, digite 1")
        print("Para Papel, digite 2")
        print("Para Tesoura, digite 3")
        print("----------------------", "\n")

        jogador1 = int(input("Jogador 1, digite a sua escolha: "))
        print("\n" * 35)
        jogador2 = int(input("Jogador 2, digite a sua escolha: "))
        print("\n" * 35)

        if jogador1 == 1:
            print("Jogador 1 escolheu: Pedra")
            print(pedra, "\n")
        elif jogador1 == 2:
            print("Jogador 1 escolheu: Papel")
            print(papel, "\n")
        elif jogador1 == 3:
            print("Jogador 1 escolheu: Tesoura")
            print(tesoura, "\n")

        if jogador2 == 1:
            print("Jogador 2 escolheu: Pedra")
            print(pedra, "\n")
        elif jogador2 == 2:
            print("Jogador 2 escolheu: Papel")
            print(papel, "\n")
        elif jogador2 == 3:
            print("Jogador 2 escolheu: Tesoura")
            print(tesoura, "\n")

        if jogador1 == 2 and jogador2 == 1 or jogador1 == 1 and jogador2 == 3 or jogador1 == 3 and jogador2 == 2:
            print("Parabéns jogador 1, você venceu!", "\n")
            pj1 += 1

        elif jogador1 == 1 and jogador2 == 2 or jogador1 == 2 and jogador2 == 3 or jogador1 == 3 and jogador2 == 1:
            print("Parabéns jogador 2, você venceu!", "\n")
            pj2 += 1

        elif jogador1 == 1 and jogador2 == 1 or jogador1 == 2 and jogador2 == 2 or jogador1 == 3 and jogador2 == 3:
            print("A partida deu empate.", "\n")
            empatesjj += 1

        else:
            print("Algum jogador digitou uma alternativa errada, por favor repita o processo.", "\n")

        print("------- PLACAR -------")
        print("Pontuação jogador 1:", pj1)
        print("Pontuação jogador 2:", pj2)
        print("Empates:", empatesjj)
        print("----------------------", "\n")

        print("(1) Sair")
        print("(2) Continuar")
        alt = int(input("Digite a alternativa: "))
        if alt == 1:
            print("\n","Saindo do jogo, obrigado por jogar e Contribuir com nosso jogo!")
            print("Feito por: Caetano, Igor Motta e Marco Antônio.")
            break

    # ─────────────────────────────────────────────
    # MODO 2 — Humano x Máquina
    # ─────────────────────────────────────────────
    elif modojogo == 2:
        print("\n","-------- REGRAS --------")
        print("Para pedra, digite 1.")
        print("Para papel, digite 2.")
        print("Para tesoura, digite 3.")
        print("------------------------", "\n")

        jogador1 = int(input("Jogador 1, digite a sua escolha: ",))
        print("\n")
        escolhamqn = random.randint(1, 3)
    
        if jogador1 == 1:
            print("Jogador 1 escolheu: Pedra")
            print(pedra, "\n")
        elif jogador1 == 2:
            print("Jogador 1 escolheu: Papel")
            print(papel, "\n")
        elif jogador1 == 3:
            print("Jogador 1 escolheu: Tesoura")
            print(tesoura, "\n")

        if escolhamqn == 1:
            print("A máquina jogou: pedra")
            print(pedra, "\n")
        elif escolhamqn == 2:
            print("A máquina jogou: papel")
            print(papel, "\n")
        else:
            print("A máquina jogou: tesoura")
            print(tesoura, "\n")

        if jogador1 == 2 and escolhamqn == 1 or jogador1 == 1 and escolhamqn == 3 or jogador1 == 3 and escolhamqn == 2:
            print("Parabéns, você venceu!")
            pj1 += 1

        elif jogador1 == 1 and escolhamqn == 2 or jogador1 == 2 and escolhamqn == 3 or jogador1 == 3 and escolhamqn == 1:
            print("Não foi desta vez :/, tente novamente.")
            pmqn += 1

        elif jogador1 == 1 and escolhamqn == 1 or jogador1 == 2 and escolhamqn == 2 or jogador1 == 3 and escolhamqn == 3:
            print("A partida deu empate.")
            empatesjm += 1

        else:
            print("Você digitou uma alternativa errada, por favor repita o processo.")

        print("------- PLACAR -------")
        print("Suas vitórias:", pj1)
        print("Vitórias da máquina:", pmqn)
        print("Empates:", empatesjm)
        print("----------------------", "\n")

        print("(1) Sair")
        print("(2) Continuar")
        alt = int(input("Digite a alternativa: "))
        if alt == 1:
            print("\n","Saindo do jogo, obrigado por jogar e contribuir com nosso jogo!")
            print("Feito por: Caetano, Igor Motta e Marco Antônio.")
            break

    # ─────────────────────────────────────────────
    # MODO 3 — Máquina x Máquina
    # ─────────────────────────────────────────────
    elif modojogo == 3:
        escolhamqn1 = random.randint(1, 3)
        print("\n")
        escolhamqn2 = random.randint(1, 3)
        print("\n")

        if escolhamqn1 == 1:
            print("Máquina 1 jogou: pedra")
            print(pedra, "\n")
        elif escolhamqn1 == 2:
            print("Máquina 1 jogou: papel")
            print(papel, "\n")
        else:
            print("Máquina 1 jogou: tesoura")
            print(tesoura, "\n")

        if escolhamqn2 == 1:
            print("Máquina 2 jogou: pedra")
            print(pedra, "\n")
        elif escolhamqn2 == 2:
            print("Máquina 2 jogou: papel")
            print(papel, "\n")
        else:
            print("Máquina 2 jogou: tesoura")
            print(tesoura, "\n")

        if escolhamqn1 == 2 and escolhamqn2 == 1 or escolhamqn1 == 1 and escolhamqn2 == 3 or escolhamqn1 == 3 and escolhamqn2 == 2:
            print("A máquina 1 venceu!")
            pmqn1 += 1

        elif escolhamqn1 == 1 and escolhamqn2 == 2 or escolhamqn1 == 2 and escolhamqn2 == 3 or escolhamqn1 == 3 and escolhamqn2 == 1:
            print("A máquina 2 venceu!")
            pmqn2 += 1

        elif escolhamqn1 == 1 and escolhamqn2 == 1 or escolhamqn1 == 2 and escolhamqn2 == 2 or escolhamqn1 == 3 and escolhamqn2 == 3:
            print("A partida deu empate.")
            empatesmm += 1

        print("-------- PLACAR --------")
        print("Vitórias da máquina 1:", pmqn1)
        print("Vitórias da máquina 2:", pmqn2)
        print("Empates:", empatesmm)
        print("------------------------", "\n")

        print("(1) Sair")
        print("(2) Continuar")
        alt = int(input("Digite a alternativa: "))
        if alt == 1:
            print("\n","Saindo do jogo, obrigado por jogar e contribuir com nosso jogo!")
            print("Feito por: Caetano, Igor Motta e Marco Antônio.")
            break
    #─────────────────────────────────────────────
    # MODO 4 — Sair
    # ────────────────────────────────────────────
    elif modojogo == 4:
        print("\n","Saindo do jogo, obrigado por jogar e Contribuir com nosso jogo!")
        print("Feito por: Caetano, Igor Motta e Marco Antonio.")
        break
    
    else:
        print("Modo inválido. Selecione uma opção entre 1 e 4.", "\n")
        print("--- Modos de jogo ---")
        print("(1) Humano x Humano")
        print("(2) Humano x Máquina")
        print("(3) Máquina x Máquina")
        print("(4) Sair")
        print("---------------------")
        modojogo = int(input("Selecione modo de jogo: "))
            