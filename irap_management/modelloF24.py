#Definizione di una classe ModelloF24 

class ModelloF24:
    def __init__(self, impresa, data):
        self.impresa = impresa 
        self.data = data
        self.importo_irap = impresa.calcola_irap() #Calcola il valore dell'importo irap per l'impresa passata come parametro

    #Metodo che restituisce un dizionario con i dati del modello F24 generato

    def prepara_f24(self):
        return {
            "codice fiscale": self.impresa.codice_fiscale,
            "denominazione": self.impresa.denominazione,
            "ragione sociale": self.impresa.ragione_sociale,
            "sede": self.impresa.sede,
            "divisione ateco": self.impresa.divisione_ateco,
            "importo irap": self.importo_irap,
            "data": self.data
        }
    