from modelloF24 import ModelloF24
from impresa import Impresa

class Comune:
    def __init__(self, nome):
        self.nome = nome
        self.imprese_registrate = []
        self.modelli_f24_emessi = []

    def registra_impresa(self, impresa):
        if not isinstance(impresa, Impresa):   
            raise ValueError("L'impresa deve essere un oggetto di tipo Impresa") #controllo se l'oggetto passato è di tipo Impresa
        self.imprese_registrate.append(impresa) #aggiungo l'impresa alla lista di imprese registrate

    def emetti_modello_f24(self, impresa, data):
        if not isinstance(impresa, Impresa):
            raise ValueError("L'impresa deve essere un oggetto di tipo Impresa")
        modello_f24 = ModelloF24(impresa, data)
        self.modelli_f24_emessi.append(modello_f24)

 
