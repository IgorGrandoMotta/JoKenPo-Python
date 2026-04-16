print("Modos de jogo:")
print("(1) humano x humano")
print("(2) humano x máquina")
print("(3) máquina x máquina")
print("(4) Sair")
pj1 = 0
pj2 = 0
empates = 0

modojogo = int(input("selecione modo de jogo: "))

while True:
     
     if modojogo == 1:
        print("REGRAS:")
        print("Para pedra, digite 1. ")
        print("Para papel, digite 2. ")
        print("Para tesoura, digite 3. ")
        jogador1 = int(input("Jogador 1, digite a sua escolha: "))
        print(" \n " * 35)
        jogador2 = int(input("Jogador 2, digite a sua escolha: "))
        print(" \n " * 35)
        
        if jogador1 == 2 and jogador2 == 1 or jogador1 == 1 and jogador2 == 3 or jogador1 == 3 and jogador2 == 2:
            print(f"Jogador 1 jogou ()")
            print("Parabéns jogador 1, você venceu!")
            pj1 += 1

        elif jogador1 == 1 and jogador2 == 2 or jogador1 == 2 and jogador2 == 3 or jogador1 == 3 and jogador2 == 1:
            print("Parabéns jogador 2, você venceu!")
            pj2 += 1

        elif jogador1 == 1 and jogador2 == 1 or jogador1 == 2 and jogador2 == 2 or jogador1 == 3 and jogador2 == 3 :
            print("A partida deu empate.")
            empates += 1

        else:
            print("")