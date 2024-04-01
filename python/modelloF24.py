from impresa import Impresa

class ModelloF24:
    def __init__(self, impresa, data):
        self.impresa = impresa 
        self.data = data
        self.importo_irap = impresa.calcola_irap()

    def prepara_f24(self):
        return {
            "codice_fiscale": self.impresa.codice_fiscale,
            "denominazione": self.impresa.denominazione,
            "ragione_sociale": self.impresa.ragione_sociale,
            "sede_legale": self.impresa.sede_legale,
            "divisione_ateco": self.impresa.divisione_ateco,
            "importo_irap": self.importo_irap,
            "data": self.data
        }
    