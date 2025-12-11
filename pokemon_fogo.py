from pokemon import Pokemon

class Pokemon_Fogo(Pokemon):
    def __init__(self, dano_base):
        super().__init__("Charmander", "Fogo", dano_base)

    def ataque_especial(self):
        self._dano += 10
        print(f"{self._nome} usou Brasas! Dano: {self._dano}")
        return self._dano
