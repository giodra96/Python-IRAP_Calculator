from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # Relazione uno-a-molti con Impresa
    imprese_registrate = db.relationship('Impresa', backref='comune', lazy=True)

    # Relazione uno-a-molti con ModelloF24
    modelli_f24_emessi = db.relationship('ModelloF24', backref='comune', lazy=True)

    def __init__(self, nome):
        self.nome = nome
    
    def serialize(self):
        return {
            'id': self.id ,
            'nome': self.nome ,
            'imprese_registrate' : [imp.id for imp in self.imprese_registrate] ,
            'modelli_f24_emessi' : [mf.id for mf in self.modelli_f24_emessi]
        }

    def registra_impresa(self, impresa):
        self.imprese_registrate.append(impresa)
        db.session.commit()

    def emetti_modello_f24(self, impresa, data):
        modello_f24 = ModelloF24(impresa=impresa, data=data)
        db.session.add(modello_f24)
        self.modelli_f24_emessi.append(modello_f24)
        db.session.commit()

class Impresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codice_fiscale = db.Column(db.String(16), unique=True, nullable=False)
    denominazione = db.Column(db.String(100), nullable=False)
    ragione_sociale = db.Column(db.String(100), nullable=False)
    sede_legale = db.Column(db.String(100), nullable=False)
    divisione_ateco = db.Column(db.String(4), nullable=False)
    numero_dipendenti = db.Column(db.Integer, nullable=False)
    numero_soci = db.Column(db.Integer, nullable=False)
    numero_amministratori = db.Column(db.Integer, nullable=False)
    data_costituzione = db.Column(db.Date, nullable=False)
    certificazioni_qualita = db.Column(db.Boolean, default=False)
    fatturato = db.Column(db.Float, nullable=False)
    comune_id = db.Column(db.Integer, db.ForeignKey('comune.id'), nullable=True)
  
    def __init__(self, codice_fiscale, denominazione, ragione_sociale, sede_legale, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato):
        self.codice_fiscale = codice_fiscale
        self.denominazione = denominazione
        self.ragione_sociale = ragione_sociale
        self.sede_legale = sede_legale
        self.divisione_ateco = divisione_ateco
        self.numero_dipendenti = numero_dipendenti
        self.numero_soci = numero_soci
        self.numero_amministratori = numero_amministratori
        self.data_costituzione = datetime.strptime(data_costituzione, "%Y-%m-%d")
        self.certificazioni_qualita = certificazioni_qualita
        self.fatturato = fatturato

    def serialize(self):
        return {
            'id': self.id,
            'codice_fiscale': self.codice_fiscale,
            'denominazione': self.denominazione,
            'ragione_sociale': self.ragione_sociale,
            'sede_legale': self.sede_legale,
            'divisione_ateco': self.divisione_ateco,
            'numero_dipendenti': self.numero_dipendenti,
            'numero_soci': self.numero_soci,
            'numero_amministratori': self.numero_amministratori,
            'data_costituzione': self.data_costituzione.strftime('%Y-%m-%d'),
            'certificazioni_qualita': self.certificazioni_qualita,
            'fatturato': self.fatturato,
            'comune_id': self.comune_id
        }
        
    def diritto_agevolazione(self):
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
        if self.diritto_agevolazione():
            riduzione_irap = irap_lorda * 1.5 / 100

        # Calcolo l'IRAP netta
        totale_irap = irap_lorda - riduzione_irap

        return totale_irap

class ModelloF24(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    impresa_id = db.Column(db.Integer, db.ForeignKey('impresa.id'), nullable=False)
    impresa = db.relationship('Impresa', backref=db.backref('modelli_f24', lazy=True))
    comune_id = db.Column(db.Integer, db.ForeignKey('comune.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    importo_irap = db.Column(db.Float, nullable=False)

    def __init__(self, impresa, data):
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.impresa = impresa
        self.importo_irap = impresa.calcola_irap()

    def serialize(self):
        return {
            "id" : self.id ,
            "impresa_id" : self.impresa.id , 
            "comune_id" : self.comune_id ,
            "data": self.data.strftime('%Y-%m-%d') ,
            "importo_irap" : self.importo_irap
        }

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