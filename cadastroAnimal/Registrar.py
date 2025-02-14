

class Registrar:
    def addInfo(self, dataI, dataO, hisMedicacao, animal);
        #metodo para passar as informacoes necessarias para o registro
        self.__dataI = dataI #data de entrada
        self.__dataO = dataO #data de saida
        self.__hisMedicacao = hisMedicacao #historico de medicação
        self.__animal = animal #animal que vai ser cadatrado

    def Registrar(self):
        with open("historico.txt", "a") as cadastro:
            cadastro.write(f"nome:{self.__animal.getNome}|dataI:{self.__dataI}dataO:{self.__dataO}|historico de medicacao:{self.__hisMedicacao}\n")
