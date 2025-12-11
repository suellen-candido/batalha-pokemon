from vantagem_elemental import vantagem
def batalha(p1, p2):
    print(f"\n(ง •̀_•́)ง BATALHA: {p1._nome} vs {p2._nome} ୧(•̀_•́ ୧)")

    print("---------- ATAQUE ----------")
    dano1 = p1.ataque_especial() * vantagem(p1._tipo, p2._tipo)
    dano2 = p2.ataque_especial() * vantagem(p2._tipo, p1._tipo)

    print("---------- DANO ----------")
    print(f"\nDano final {p1._nome}: {dano1}")
    print(f"Dano final {p2._nome}: {dano2}")

    print("---------- CAMPEÃO ----------")
    if dano1 > dano2:
        print(f"\n˗ˏˋ ★ ˎˊ˗ {p1._nome} venceu!")
    elif dano2 > dano1:
        print(f"\n˗ˏˋ ★ ˎˊ˗ {p2._nome} venceu!")
    else:
        print("\n(ง ˃ ᗜ ˂)ว  .ˊˎ- ヾ(•̀ ヮ <)و Empate!")
