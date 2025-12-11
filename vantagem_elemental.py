def vantagem(tipo1, tipo2):
    regras = {
        "Água": "Fogo",
        "Fogo": "Planta",
        "Planta": "Água"
    }

    if tipo1 == tipo2:
        return 1
    elif regras[tipo1] == tipo2:
        return 2      # vantagem
    else:
        return 0.5    # desvantagem
