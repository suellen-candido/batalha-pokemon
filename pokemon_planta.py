from pokemon import Pokemon

class Pokemon_Planta(Pokemon):
    def __init__(self, dano_base):
        super().__init__("Bulbasaur", "Planta", dano_base)

    def ataque_especial(self):
        self._dano += 20
        print(f"{self._nome} usou Chicote de Vinha! Dano: {self._dano}")
        return self._dano
