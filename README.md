# Simulador Simples de Batalha Pokémon (Terminal)

Um minigame de batalha Pokémon no terminal, desenvolvido em Python usando conceitos fundamentos de POO, como: herança, polimorfismo e encapsulamento.

## O que é? ∘ ∘ ∘ ( °ヮ° ) ?

Esse pequeno projeto simula uma batalha ente dois Pokémons escolhidos pelo próprio usuário, diretamente no terminal.
Cada Pokémon possui um tipo para ser escolhido (Água, Fogo ou Planta), dano base e um ataque especial que modifica o dano final considerando vantagens elementais, assim como na franquia pokémon mesmo.

## Funcionalidades ☆:

- Escolha interativa de dois Pokémons pelo usuário, com opções de tipo: Água, Fogo ou Planta.
- Cálculo de dano baseado em:
  - Dano base do Pokémon.
  - Bônus do ataque especial de cada tipo.
  - Multiplicador de vantagem/desvantagem elemental.
- Exibição no terminal do processo de batalha, dano final de cada Pokémon e anúncio do vencedor ou empate. 

## Estrutura do Projeto ₊˚⊹

- `main.py`: ponto de entrada da aplicação, exibe o menu inicial, permite escolher os Pokémons e inicia a batalha.
- `pokemon.py`: classe base `Pokemon`, contendo atributos comuns (nome, tipo, dano_base), método de ataque genérico e interface para o ataque especial. 
- `pokemon_agua.py`: classe `Pokemon_Agua`, representa o Squirtle com tipo Água e ataque especial que aumenta o dano em um valor fixo.
- `pokemon_fogo.py`: classe `Pokemon_Fogo`, representa o Charmander com tipo Fogo e ataque especial próprio. 
- `pokemon_planta.py`: classe `Pokemon_Planta`, representa o Bulbasaur com tipo Planta e ataque especial próprio.
- `vantagem_elemental.py`: função `vantagem(tipo1, tipo2)` que retorna multiplicadores 2, 1 ou 0.5 conforme a relação entre Água, Fogo e Planta. 
- `batalha.py`: função `batalha(p1, p2)` que executa os ataques especiais, aplica a vantagem elemental, mostra os danos finais e define o campeão.

## Requisitos ⋆

- Python 3.x instalado na máquina.  
- Todos os arquivos `.py` na mesma pasta para que os imports funcionem corretamente.

## Como Executar ⋆ .ᐟ.ᐟ

1. Clone ou baixe o projeto para uma pasta local.  
2. Abra o terminal na pasta do projeto.  
3. Execute

4. Siga as instruções do terminal:
- Escolha o tipo do primeiro Pokémon ([1] Água, [2] Fogo, [3] Planta).  
- Escolha o tipo do segundo Pokémon.  
- Veja os ataques especiais, o dano final de cada um e o resultado da batalha.

5. E o mais importante, se divirta! ദ്ദി( • ᴗ < )

