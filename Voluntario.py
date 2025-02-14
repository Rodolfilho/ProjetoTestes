class Voluntario:
    def __init__(self, nome, contato, funcao):
        self.__nome = nome
        self.__contato = contato
        self.__funcao = funcao #atuar em resgate ou prestar assintecia no centro
        self.__escalaTrabalho = 0
    
    def setEscalaTrab(self, escala):
        self.__escalaTrabalho = escala