from pokemon_agua import Pokemon_Agua
from pokemon_fogo import Pokemon_Fogo
from pokemon_planta import Pokemon_Planta
from batalha import batalha

print("-="*15)
print("Seja-Bem Vindo(a) ao\nSimulador de Batalha Pokémon")
print("-="*15)
def escolher():
    print("[1] Água\n[2] Fogo\n[3] Planta")
    escolha = int(input("Escolha um tipo de pokémon:\nR- "))
    print('-'*30)

    if escolha == 1:
        return Pokemon_Agua(10)
    elif escolha == 2:
        return Pokemon_Fogo(10)
    elif escolha == 3:
        return Pokemon_Planta(10)

def main():
    p1 = escolher()
    p2 = escolher()
    batalha(p1, p2)

if __name__ == "__main__":
    main()
