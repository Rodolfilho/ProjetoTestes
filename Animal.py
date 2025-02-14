class Animal:
    def __init__(self, especie, raca, idade, sexo, caracterisca, status):
        self.__especie = especie
        self.__raca = raca
        self.__idadeEstimada = idade
        self.__sexo = sexo
        self.__caracteristicas = caracterisca
        self.__status = status#diponovel, adotado ou indisponivel

    def getNome(self):
        return nome