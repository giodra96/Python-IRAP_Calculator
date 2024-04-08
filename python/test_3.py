from comune import Comune #Importo la classe Comune dal file comune.py
from impresa import Impresa #Importo la classe Impresa dal file impresa.py
from datetime import datetime, date #Importo datetime per la gestione e il controllo delle date

#Metodo per la validazione dei dati inseriti da input

def valida_dato(valore, tipo_dato, messaggio_errore):
    try:
        if tipo_dato == "intero": #Controllo per tipo int
            if valore < 1:
                raise ValueError("Numero non valido")
            return int(valore)
        elif tipo_dato == "data": #Controllo per tipo data
            datetime.strptime(valore, "%d-%m-%Y")
            return valore
        elif tipo_dato == "booleano": #Controllo per tipo bool
            return bool(valore.lower() in ["true", "True", "si", "Si", "s", "S"])
        elif tipo_dato == "codice_fiscale": #Controllo per tipo codice fiscale
            if len(str(valore)) != 11:
                raise ValueError("Codice fiscale non valido")
            return int(valore)
    except ValueError:
        raise ValueError(messaggio_errore) #Ritorna il messaggio di errore passato come parametro

#Metodo per l'aggiunta di un nuovo comune

def aggiungi_comune(lista_comuni):
    #Inizializzo una variabile di controllo che serve a permettere l'inserimento di più comuni
    stop = False 
    while(stop == False):
        #Inizializzo una seconda variabile di controllo che serve a non uscire uscire dal ciclo 
        #fintanto che non è stato inserito un nome non presente pre il comune
        stop2 = False 
        while(stop2 == False):
            stop2 = True
            nome = input("Quale è il nome del comune? ")
            for comune in lista_comuni:
                if nome == comune.nome: #Verifica della presenza del comune
                    print("Il comune è già presente")
                    stop2 = False
                    break
        comune = Comune(nome)
        lista_comuni.append(comune) #Aggiungo il nuovo comune alla lista
        stop = input("Vuoi inserire altri comuni? (S/N): ") in ["n", "N"] #Se voglio aggiungere un altro comune setterò stop uguale a false
    return lista_comuni

#Metodo per la registrazione di un'impresa presso il comune

def registra_impresa(lista_comuni, lista_imprese):
    stop = False #Inizializzo una variabile di controllo per la verifica della presenza dell'impresa già a sistema
    stop2 = False #Inizializzo una variabile di controllo per verificare la presenza del comune
    codice_fiscale = valida_dato(input("Quale è il codice fiscale dell'impresa? "), "codice_fiscale", "Codice fiscale non valido")
    for impresa in lista_imprese:
        if impresa.codice_fiscale == codice_fiscale:
            print("Impresa già registrata a sistema")
            stop = True
            break
    if (stop == False): #Creazione di un nuovo oggetto impresa con l'inserimento dei dati da input
        sede_legale = input("Quale è la sede legale(nome del comune) dell'impresa? ")
        if not sede_legale[0].isupper(): #Verifica che la prima lettera sia maiuscola
            sede_legale = sede_legale.capitalize() #Setaggio della prima lettera maiuscola
        for comune in lista_comuni:
            if comune.nome == sede_legale: #Verifica che esiste il comune per la registrazione dell'impresa
                stop2 == True
                denominazione = input("Quale è il nome dell'impresa?")
                if not denominazione[0].isupper(): 
                    denominazione = denominazione.capitalize()
                stop2 = False #Inizializzo una variabile di controllo per verificare che venga inserito un valore valido per la ragione sociale
                while(stop2 == False):
                    ragione_sociale = input("Quale è la ragione sociale dell'impresa? \n Valori ammessi: Societa per Azioni, Societa Cooperativa, Società Responsabilita Limitata, Impresa Individuale")
                    if ragione_sociale != "Societa per Azioni" or ragione_sociale != "Societa Cooperativa" or ragione_sociale != "Società Responsabilita Limitata" or ragione_sociale != "Impresa Individuale":
                        print("Valore non ammesso \n") #Messaggio di errore
                    else: stop2 = True
                divisione_ateco = input("Quale è la divisione ateco dell'impresa? ")
                if not divisione_ateco.isupper(): #Verifica che tutte le lettere siano maiuscole
                    divisione_ateco = divisione_ateco.upper() #Settaggio di tutte le lettere in maiuscolo
                numero_dipendenti = valida_dato(input("Quale è il numero di dipendenti dell'impresa? "), "intero", "Numero di dipendenti non valido")
                numero_soci = valida_dato(input("Quale è il numero di soci dell'impresa? "), "intero", "Numero di soci non valido")
                numero_amministratori = valida_dato(input("Quale è il numero di amministratori dell'impresa? "), "intero", "Numero di amministratori non valido")
                data_costituzione = valida_dato(input("Quale è la data di costituzione dell'impresa? \n Inserire una data nel formato gg-mm-aaaa"), "data", "Data di costituzione non valida")
                certificazioni_qualita = valida_dato(input("L'impresa ha certificazioni di qualità? (S\N) "), "booleano", "Certificazioni di qualità non valide")
                fatturato = valida_dato(input("Quale è il fatturato dell'impresa? "), "intero", "Fatturato non valido")
                impresa = Impresa(codice_fiscale, denominazione, ragione_sociale, sede_legale, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato)
                comune.registra_impresa(impresa) #Registrazione dell'impresa presso il comune
                lista_imprese.append(impresa) #Aggiunta dell'impresa all'array lista_imprese
                break
    if stop2 == False: print("Il comune della sede legale dell'impresa non è registrato a sistema") 
    return {"imprese": lista_imprese, "comuni": lista_comuni}

#Metodo che calcola l'IRAP per l'impresa

def calcola_irap (lista_imprese):
    stop = False #Inizializzo una variabile di controllo per verificare la presenza dell'impresa
    nome = input("Di quale impresa vuoi calcolare l'IRAP? ")
    if not nome[0].isupper(): 
        nome = nome.capitalize()
    for impresa in lista_imprese:
        if nome == impresa.denominazione: #Verifica se l'impresa è presente
            totale_irap = impresa.calcola_irap()
            stop = True
            break
    if stop != False: #Se l'impresa non è presente stampo un errore
        return totale_irap
    else: print("L'impresa non è registrata a sistema")

#Metodo che emette un ModelloF24 per l'impresa

def emissione_modellof24(lista_comuni, lista_imprese):
    stop = False #Inizializzo una variabile di controllo per verificare la presenza dell'impresa
    stop2 = False #Inizializzo una variabile di controllo per verificare la presenza del comune
    nome = input("Di quale impresa vuoi emettere il modelloF24? ")
    if not nome[0].isupper(): 
        nome = nome.capitalize()
    for impresa in lista_imprese:
        if nome == impresa.denominazione: #Verifica se l'impresa è presente
            stop = True
            for comune in lista_comuni:
                if comune.nome == impresa.sede_legale: #Verifica se il comune è presente
                    stop2 = True
                    comune.emetti_modello_f24(impresa, date.today()) #Emetto il ModelloF24 con la data odierna
                    print("Modello F24 emesso")
                    break
        if stop2 == True: break
    if stop == False: print("L'impresa non è registrata a sistema")
    if stop2 == False: print("Il comune della sede legale dell'impresa non è registrato a sistema")

#Metodo che emette un ModelloF24 a ritroso per l'impresa

def emissione_modellof24_ritroso(lista_comuni):
    print("Inserisci i dati dell'azienda per l'emissione del Modello F24 in una data antecedente. \n\n")
    stop = False
    codice_fiscale = valida_dato(input("Quale è il codice fiscale dell'impresa? "), "codice_fiscale", "Codice fiscale non valido")
    sede_legale = input("Quale è la sede legale dell'impresa? ")
    if not sede_legale[0].isupper():
        sede_legale = sede_legale.capitalize()
    for comune in lista_comuni:
        if comune.nome == sede_legale:
            stop = True
            denominazione = input("Quale è il nome dell'impresa? ")
            if not denominazione[0].isupper(): 
                denominazione = denominazione.capitalize()
            stop2 = False
            while(stop2 == False):
                ragione_sociale = input("Quale è la ragione sociale dell'impresa? \n Valori ammessi: Societa per Azioni, Societa Cooperativa, Società Responsabilita Limitata, Impresa Individuale")
                if ragione_sociale != "Societa per Azioni" or ragione_sociale != "Societa Cooperativa" or ragione_sociale != "Società Responsabilita Limitata" or ragione_sociale != "Impresa Individuale":
                    print("Valore non ammesso \n")
                else: stop2 = True    
            divisione_ateco = input("Quale è la divisione ateco dell'impresa? ")
            if not divisione_ateco.isupper(): #Verifica che tutte le lettere siano maiuscole
                divisione_ateco = divisione_ateco.upper()
            numero_dipendenti = valida_dato(input("Quale è il numero di dipendenti dell'impresa? "), "intero", "Numero di dipendenti non valido")
            numero_soci = valida_dato(input("Quale è il numero di soci dell'impresa? "), "intero", "Numero di soci non valido")
            numero_amministratori = valida_dato(input("Quale è il numero di amministratori dell'impresa? "), "intero", "Numero di amministratori non valido")
            data_costituzione = valida_dato(input("Quale è la data di costituzione dell'impresa? \n Inserire una data nel formato gg-mm-aaaa"), "data", "Data di costituzione non valida")
            certificazioni_qualita = valida_dato(input("L'impresa ha certificazioni di qualità? "), "booleano", "Certificazioni di qualità non valide")
            fatturato = valida_dato(input("Quale è il fatturato dell'impresa? "), "intero", "Fatturato non valido")
            impresa = Impresa(codice_fiscale, denominazione, ragione_sociale, sede_legale, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato)
            data = valida_dato(input("In che data del passato vuoi emettere il modello? \n Inserire una data nel formato gg-mm-aaaa"), "data", "Data non valida")
            comune.emetti_modello_f24(impresa, data) #Emissione del ModelloF24 con data nel passato
            print("Modello F24 emesso")
            break
    if stop == False: print("Non esiste il comune corrispodente alla sede legale esplicitata per l'impresa a sistema ")

#Metodo che stampa i ModelliF24 emessi per ogni comune

def stampa_modelliF24(nome_comune, lista_comuni):
    for comune in lista_comuni:
        if comune.nome == nome_comune:
            print(f"Ecco la lista dei ModelliF24 emessi dal comune di {comune.nome}")
            for modello in comune.modelli_f24_emessi:
                print(modello.prepara_f24()) #Prepara_f24 restituisce un dizionario con i dati del modello
        break

#Metodo che restituisce un report con le statistiche sull'IRAP riscosso dal comune nel periodo

def genera_report(nome_comune, lista_comuni, inizio, fine):
    print(f"Report sull'IRAP riscosso dal comune di {nome_comune} dal {inizio} al {fine} \n\n")
    somma = 0
    conta = 0
    for comune in lista_comuni:
        if comune.nome == nome_comune:
            for modello in comune.modelli_f24_emessi:
                if modello.data <= fine and modello.data >= inizio:
                    somma += modello.importo_irap
                    conta += 1
        break
    print(f"Numero di aziende paganti nel periodo: {conta} \n")
    print(f"Totale IRAP pagato nel periodo: {somma} \n")
    print(f"Quota IRAP media per azienda nel periodo: {somma/conta} \n")