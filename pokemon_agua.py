from pokemon import Pokemon

class Pokemon_Agua(Pokemon):
    def __init__(self, dano_base):
        super().__init__("Squirtle", "Água", dano_base)

    def ataque_especial(self):
        self._dano += 15
        print(f"{self._nome} usou Jato d'Água! Dano: {self._dano}")
        return self._dano
