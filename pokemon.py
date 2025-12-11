class Pokemon:
    def __init__(self, nome, tipo, dano_base):
        self._nome = nome
        self._tipo = tipo
        self._dano = dano_base

    @property
    def dano(self):
        return self._dano

    def atacar(self):
        self._dano += 5
        print(f"{self._nome} atacou! Dano atual: {self._dano}")
        return self._dano

    def ataque_especial(self):
        raise NotImplementedError("Cada Pokémon deve ter seu próprio ataque especial!")

    def __str__(self):
        return f"{self._nome} ({self._tipo}) com dano {self._dano}"
