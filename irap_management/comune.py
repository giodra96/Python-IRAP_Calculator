from modelloF24 import ModelloF24 #import della classe ModelloF24

#Definizione della classe Comune

class Comune:
    def __init__(self, nome):
        self.nome = nome
        self.imprese_registrate = [] #Lista di imprese registrate presso il comune
        self.modelli_f24_emessi = [] #Lista dei modelli f24 emessi presso il comune

    #Metodo per registrare l'impresa presso il comune

    def registra_impresa(self, impresa):
        self.imprese_registrate.append(impresa) #Aggiungo l'impresa alla lista di imprese registrate

    #Metodo per emettere un modello f24 presso il comune

    def emetti_modello_f24(self, impresa, data):
        modello_f24 = ModelloF24(impresa, data) #Creo un nuovo modello f24 presso il comune
        self.modelli_f24_emessi.append(modello_f24) #Aggiungo il modello f24 alla lista dei modelli f24 emessi