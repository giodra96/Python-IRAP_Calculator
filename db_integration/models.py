from datetime import datetime #Import di datetime per la gestione delle date
from flask_sqlalchemy import SQLAlchemy #Import di SQLAlchemy per la creazione delle tabelle

db = SQLAlchemy() 

class Comune(db.Model): #Definizione della tabella comune nel db
    id = db.Column(db.Integer, primary_key=True) #Definizione della primary key
    nome = db.Column(db.String(30), unique=True, nullable=False) #Nome del comune
    #Relazione uno-a-molti con Impresa
    imprese_registrate = db.relationship('Impresa', backref='comune', lazy=True) #Elenco delle imprese registrate
    #Relazione uno-a-molti con ModelloF24
    modelli_f24_emessi = db.relationship('ModelloF24', backref='comune', lazy=True) #Elenco dei ModelliF24 emessi

    def __init__(self, nome): #Definizione del costruttore per comune 
        self.nome = nome
    
    def serialize(self): #Creazione di un dizionario 
        return {
            'id': self.id,
            'nome': self.nome,
            'imprese_registrate' : [imp.id for imp in self.imprese_registrate],
            'modelli_f24_emessi' : [mf.id for mf in self.modelli_f24_emessi]
        }

    def registra_impresa(self, impresa): #Metodo per registrare un'impresa al comune
        try: #Controllo di possibili errori sul db
            self.imprese_registrate.append(impresa) #Aggiunta impresa alla lista delle imprese registrate per il comune
            db.session.commit() #Salvataggio delle modifiche a db
        except Exception as e: raise e

    def emetti_modello_f24(self, impresa, data): #Metodo per emettere un modelloF24 al comune
        try:
            modello_f24 = ModelloF24(impresa, data) #Creazione di un nuovo oggetto ModelloF24
            db.session.add(modello_f24) #Aggiunta dell'oggeto a db
            self.modelli_f24_emessi.append(modello_f24) #Aggiunta del modelloF24 a quelli emessi per il comune
            db.session.commit()
        except Exception as e: raise e

class Impresa(db.Model): #Creazione della tabella imppresa nel db
    id = db.Column(db.Integer, primary_key=True) #Definizione della primary key
    codice_fiscale = db.Column(db.String(11), unique=True, nullable=False)
    denominazione = db.Column(db.String(30), unique=True, nullable=False)
    ragione_sociale = db.Column(db.String(20), nullable=False)
    sede = db.Column(db.String(30), nullable=False)
    divisione_ateco = db.Column(db.String(3), nullable=False)
    numero_dipendenti = db.Column(db.Integer, nullable=False)
    numero_soci = db.Column(db.Integer, nullable=False)
    numero_amministratori = db.Column(db.Integer, nullable=False)
    data_costituzione = db.Column(db.Date, nullable=False)
    certificazioni_qualita = db.Column(db.Boolean, default=False)
    fatturato = db.Column(db.Float, nullable=False)
    comune_id = db.Column(db.Integer, db.ForeignKey('comune.id'), nullable=True) #Definizione della foreign key per comune
  
    def __init__(self, codice_fiscale, denominazione, ragione_sociale, sede, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato):
        self.codice_fiscale = codice_fiscale
        self.denominazione = denominazione
        self.ragione_sociale = ragione_sociale
        self.sede = sede
        self.divisione_ateco = divisione_ateco
        self.numero_dipendenti = numero_dipendenti
        self.numero_soci = numero_soci
        self.numero_amministratori = numero_amministratori
        self.data_costituzione = datetime.strptime(data_costituzione, "%Y-%m-%d") #Conversione della data in formato stringa in formato datetime
        self.certificazioni_qualita = certificazioni_qualita
        self.fatturato = fatturato

    def serialize(self):
        return {
            'id': self.id,
            'codice_fiscale': self.codice_fiscale,
            'denominazione': self.denominazione,
            'ragione_sociale': self.ragione_sociale,
            'sede': self.sede,
            'divisione_ateco': self.divisione_ateco,
            'numero_dipendenti': self.numero_dipendenti,
            'numero_soci': self.numero_soci,
            'numero_amministratori': self.numero_amministratori,
            'data_costituzione': self.data_costituzione.strftime('%Y-%m-%d'), #Conversione della data in formato datetime in formato stringa
            'certificazioni_qualita': self.certificazioni_qualita,
            'fatturato': self.fatturato,
            'comune_id': self.comune_id
        }
        
    #Il metodo diritto_agevolazione verifica se l'impresa rientra in un diritto agevolazione per le imprese
    #con codice ATECO "A03" e con un numero di dipendenti maggiore di 15

    def diritto_agevolazione(self):
        # Verifica se la divisione ATECO è "A03" e se il numero di dipendenti è maggiore di 15
        if self.divisione_ateco == "A03" and self.numero_dipendenti > 15:
            return True
        else:
            return False

    #Il metodo calcola_irap calcola il valore dell'IRAP al netto  
    #delle riduzioni previste per le imprese agevolate 

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
        if Impresa.diritto_agevolazione(self):
            riduzione_irap = irap_lorda * 1.5 / 100
        # Calcolo l'IRAP netta
        totale_irap = irap_lorda - riduzione_irap
        return totale_irap

class ModelloF24(db.Model): #Creazione della tabella ModelloF24 nel db
    id = db.Column(db.Integer, primary_key=True) #Definizione della primary key
    impresa_id = db.Column(db.Integer, db.ForeignKey('impresa.id'), nullable=False) #Definizione della foreign key per impresa
    comune_id = db.Column(db.Integer, db.ForeignKey('comune.id'), nullable=False) #Definizione della foreign key per comune
    data = db.Column(db.Date, nullable=False)
    importo_irap = db.Column(db.Float, nullable=False)
    #Relazione uno-a-molti con Impresa
    impresa = db.relationship('Impresa', backref='modelli_f24', lazy=True) 
    
    def __init__(self, impresa, data):
        self.data = datetime.strptime(data, "%Y-%m-%d") #Conversione della data in formato stringa in formato datetime
        self.impresa = impresa
        self.importo_irap = impresa.calcola_irap()

    def serialize(self):
        return {
            "id" : self.id ,
            "impresa_id" : self.impresa.id, 
            "comune_id" : self.comune_id,
            "data": self.data.strftime('%Y-%m-%d'), #Conversione della data in formato datetime in formato stringa
            "importo_irap" : self.importo_irap
        }

    #Metodo che restituisce un dizionario con i dati del modello F24 generato

    def prepara_f24(self):
        return {
            "codice fiscale": self.impresa.codice_fiscale,
            "denominazione": self.impresa.denominazione,
            "ragione sociale": self.impresa.ragione_sociale,
            "sede": self.impresa.sede_legale,
            "divisione ateco": self.impresa.divisione_ateco,
            "importo irap": self.importo_irap,
            "data": self.data
        }