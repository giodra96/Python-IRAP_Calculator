from modelloF24 import ModelloF24
from impresa import Impresa

class Comune:
    def __init__(self, nome):
        self.nome = nome
        self.imprese_registrate = []
        self.modelli_f24_emessi = []

    def registra_impresa(self, impresa):
        self.imprese_registrate.append(impresa) #aggiungo l'impresa alla lista di imprese registrate

    def emetti_modello_f24(self, impresa, data):
        modello_f24 = ModelloF24(impresa, data)
        self.modelli_f24_emessi.append(modello_f24)

 
