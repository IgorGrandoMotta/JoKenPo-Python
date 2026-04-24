Jogo Pedra, Papel e Tesoura em Python

-Descrição:

Este projeto consiste em um jogo de Pedra, Papel e Tesoura desenvolvido em Python, com diferentes modos de jogo e sistema de pontuação. O programa permite partidas entre jogadores humanos e também simulações com a máquina.

O código utiliza estruturas de repetição, condicionais e geração de números aleatórios para controlar o fluxo do jogo.

-Funcionalidades:

Modo 1: Humano vs Humano

Modo 2: Humano vs Máquina

Modo 3: Máquina vs Máquina

Sistema de pontuação para cada modo

Contagem de empates

Interface via terminal

Representação visual das jogadas com ASCII

-Demonstração
Tela inicial do jogo:
<img width="876" height="191" alt="image" src="https://github.com/user-attachments/assets/cb33e22a-a4fd-4347-85e0-635be3ab4302" />

Exemplo de placar:
<img width="194" height="131" alt="image" src="https://github.com/user-attachments/assets/cdc04c71-5ba6-4e86-beb6-de25ec86b198" />

-Estrutura do código

O jogo utiliza desenhos em ASCII para mostrar as escolhas:
<img width="222" height="567" alt="image" src="https://github.com/user-attachments/assets/cb0135d8-a982-44f5-9389-90cf361a379d" />

-Controle de pontuação

O programa mantém variáveis para armazenar:
Vitórias dos jogadores, Vitórias da máquinae e Empates
<img width="123" height="173" alt="image" src="https://github.com/user-attachments/assets/c420ff25-fc7d-4eb4-adbc-c417883b9612" />
*pj1

Armazena o número de vitórias do Jogador 1.

Usada nos modos:
Humano vs Humano e
Humano vs Máquina

*pj2

Armazena o número de vitórias do Jogador 2.

Usada apenas no modo:
Humano vs Humano

*pmqn

Armazena o número de vitórias da máquina no modo Humano vs Máquina.

Representa quantas vezes a máquina venceu o jogador.

*pmqn1

Armazena as vitórias da Máquina 1 no modo Máquina vs Máquina.

*pmqn2

Armazena as vitórias da Máquina 2 no modo Máquina vs Máquina.

*empatesjj

Conta os empates no modo Jogador vs Jogador.

*empatesjm

Conta os empates no modo Jogador vs Máquina.

*empatesmm

Conta os empates no modo Máquina vs Máquina.

-Lógica do jogo

A decisão de vitória é feita com base nas regras clássicas:

Pedra vence Tesoura

Tesoura vence Papel

Papel vence Pedra

Parte do código:
<img width="372" height="434" alt="image" src="https://github.com/user-attachments/assets/b0e35f29-8b45-4e42-b83c-671bc31e3728" />

-Uso de aleatoriedade

No modo contra máquina, o programa usa a biblioteca random para gerar jogadas automaticamente.
<img width="188" height="36" alt="image" src="https://github.com/user-attachments/assets/4e9ce5a4-e632-4a24-a9a2-ee80d037ddb6" />
