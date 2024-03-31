class Impresa:
    def __init__(self, codice_fiscale, denominazione, ragione_sociale, sede_legale, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato):
        self.codice_fiscale = codice_fiscale
        self.denominazione = denominazione
        self.ragione_sociale = ragione_sociale
        self.sede_legale = sede_legale
        self.divisione_ateco = divisione_ateco
        self.numero_dipendenti = numero_dipendenti
        self.numero_soci = numero_soci
        self.numero_amministratori = numero_amministratori
        self.data_costituzione = data_costituzione
        self.certificazioni_qualita = certificazioni_qualita
        self.fatturato = fatturato

    def dirittoAgevolazione(self):

        # Verifica se la divisione ATECO è "A03" e se il numero di dipendenti è maggiore di 15
        if self.divisione_ateco == "A03" and self.numero_dipendenti > 15:
            return True
        else:
            return False

    def calcola_irap(self):

        # Ricerca l'aliquota IRAP specifica per la divisione ATECO
        if self.fatturato < 10000: 
            aliquota_irap = 0 
            coefficiente_irap = 0
        elif self.fatturato < 50000:
            aliquota_irap = .0049
            coefficiente_irap = 1.2
        elif self.fatturato < 150000:
            aliquota_irap = .0076
            coefficiente_irap = 1.5
        else:
            aliquota_irap = .0081
            coefficiente_irap = 1.7

        # Applicazione aliquota IRAP
        irap_lorda = self.fatturato * aliquota_irap * coefficiente_irap

        # Riduzione IRAP
        riduzione_irap = 0
        if Impresa.dirittoAgevolazione(self) == True:
            riduzione_irap = irap_lorda * 1.5 / 100

        # Calcolo l'IRAP netta
        totale_irap = irap_lorda - riduzione_irap

        return totale_irap