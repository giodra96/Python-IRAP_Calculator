from comune import Comune #Import della classe Comune dal file comune.py
from impresa import Impresa #Import della classe Impresa dal file impresa.py
from datetime import datetime, date #Import di datetime per la gestione e il controllo delle date
import test_2 #Import dei metodi definiti nel test_2

#Metodo per la validazione dei dati inseriti da input

def valida_dato(valore, tipo_dato, messaggio_errore):
    try:
        if tipo_dato == "intero": #Controllo per tipo int
            valore = int(valore)
            if valore < 1:
                raise ValueError("Numero non valido.")
            return valore
        elif tipo_dato == "data": #Controllo per tipo data
            datetime.strptime(valore, "%d-%m-%Y")
            return valore
        elif tipo_dato == "booleano": #Controllo per tipo bool
            return bool(valore.lower() in ["true", "True", "si", "Si", "s", "S"])
        elif tipo_dato == "codice_fiscale": #Controllo per tipo codice fiscale
            if len(str(valore)) != 11:
                raise ValueError("Codice fiscale non valido.")
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
                    print("Il comune è già presente a sistema. \n")
                    stop2 = False
                    break
        comune = Comune(nome)
        lista_comuni.append(comune) #Aggiungo il nuovo comune alla lista
        stop = input("Vuoi inserire altri comuni? (S/N): \n") in ["n", "N"] #Se voglio aggiungere un altro comune setterò stop uguale a false
    return lista_comuni

#Metodo per la registrazione di un'impresa presso il comune

def registra_impresa(lista_comuni, lista_imprese):
    if len(lista_comuni) == 0: raise ValueError("Non sono presenti comuni registrati a sistema.") #Verifica della presenza di comuni nell'array
    codice_fiscale = valida_dato(input("Quale è il codice fiscale dell'impresa? (11 cifre) "), "codice_fiscale", "Codice fiscale non valido")
    denominazione = input("Quale è il nome dell'impresa? ")
    if not denominazione[0].isupper(): 
        denominazione = denominazione.capitalize()
    for impresa in lista_imprese:
        #Verifica che non esistono imprese già registrate con lo stesso codice fiscale e denominazione
        if impresa.codice_fiscale == codice_fiscale and impresa.denominazione == denominazione: 
            print("Impresa già registrata a sistema \n")
            return {"imprese": lista_imprese, "comuni": lista_comuni}
    sede = input("Quale è la sede (nome del comune) dell'impresa? ")
    if not sede[0].isupper(): #Verifica che la prima lettera sia maiuscola
        sede = sede.capitalize() #Setaggio della prima lettera maiuscola
    for comune in lista_comuni:
        if comune.nome == sede: #Verifica che esiste il comune per la registrazione dell'impresa
            stop = False #Inizializzo una variabile di controllo per verificare che venga inserito un valore valido per la ragione sociale
            while(stop == False):
                valori_ammessi = ["Societa per Azioni", "Societa Cooperativa", "Societa Responsabilita Limitata", "Impresa Individuale"]
                ragione_sociale = input(f"Quale è la ragione sociale dell'impresa? \nValori ammessi: {valori_ammessi}: ")
                if ragione_sociale not in valori_ammessi:
                    print("Valore non ammesso. \n") #Messaggio di errore
                else: stop = True  
            divisione_ateco = input("Quale è la divisione ateco dell'impresa? ")
            if not divisione_ateco.isupper(): #Verifica che tutte le lettere siano maiuscole
                divisione_ateco = divisione_ateco.upper() #Settaggio di tutte le lettere in maiuscolo
            numero_dipendenti = valida_dato(input("Quale è il numero di dipendenti dell'impresa? "), "intero", "Numero di dipendenti non valido")
            numero_soci = valida_dato(input("Quale è il numero di soci dell'impresa? "), "intero", "Numero di soci non valido")
            numero_amministratori = valida_dato(input("Quale è il numero di amministratori dell'impresa? "), "intero", "Numero di amministratori non valido")
            data_oggi = date.today() #Salvataggio della data odierna
            data_oggi = data_oggi.strftime("%d-%m-%Y") #Conversione in una stringa
            data_oggi = datetime.strptime(data_oggi, "%d-%m-%Y") #Conversione in datetime per poterlo confrontare
            stop = False
            while(stop == False): #Finché la data inserita è maggiore di quella odierna il sistema la richiede
                data_costituzione = valida_dato(input("Quale è la data di costituzione dell'impresa? (formato gg-mm-aaaa) "), "data", "Data di costituzione non valida")
                if datetime.strptime(data_costituzione, "%d-%m-%Y") > data_oggi: print("Data successiva a quella odierna. ")
                else: stop = True
            certificazioni_qualita = valida_dato(input("L'impresa ha certificazioni di qualità? (S/N) "), "booleano", "Valore inserito non valido")
            fatturato = valida_dato(input("Quale è il fatturato dell'impresa? (espresso in € e senza decimali) "), "intero", "Fatturato non valido")
            impresa = Impresa(codice_fiscale, denominazione, ragione_sociale, sede, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato)
            comune.registra_impresa(impresa) #Registrazione dell'impresa presso il comune
            lista_imprese.append(impresa) #Aggiunta dell'impresa all'array lista_imprese
            return {"imprese": lista_imprese, "comuni": lista_comuni}
    print("Il comune della sede dell'impresa non è registrato a sistema. Per procedere registralo come nuovo comune. \n") 
    return {"imprese": lista_imprese, "comuni": lista_comuni}

#Metodo che calcola l'IRAP per l'impresa

def calcola_irap(lista_imprese):
    if len(lista_imprese) == 0: raise ValueError("Non sono presenti imprese registrate a sistema. ") #Verifica della presenza di imprese nell'array
    nome = input("Di quale impresa vuoi calcolare l'IRAP? ")
    if not nome[0].isupper(): 
        nome = nome.capitalize()
    for impresa in lista_imprese:
        if nome == impresa.denominazione: #Verifica se l'impresa è presente
            totale_irap = impresa.calcola_irap()
            print(f"Totale IRAP per l'impresa {nome}: {totale_irap}€ \n")
            return
    print(f"L'impresa {nome} non è registrata a sistema. \n")

#Metodo che emette un ModelloF24 per l'impresa

def emissione_modellof24(lista_comuni, lista_imprese):
    if len(lista_comuni) == 0: raise ValueError("Non sono presenti comuni registrati a sistema. ") #Verifica della presenza di comuni nell'array
    if len(lista_imprese) == 0: raise ValueError("Non sono presenti imprese registrate a sistema. ") #Verifica della presenza di imprese nell'array
    nome = input("Di quale impresa vuoi emettere il modelloF24? ")
    if not nome[0].isupper(): 
        nome = nome.capitalize()
    for impresa in lista_imprese:
        if nome == impresa.denominazione: #Verifica se l'impresa è presente
            for comune in lista_comuni:
                if comune.nome == impresa.sede: #Verifica se il comune è presente
                    data_oggi = date.today()
                    data_oggi = data_oggi.strftime("%d-%m-%Y") #Trasformo la data in una stringa
                    data_oggi = datetime.strptime(data_oggi, "%d-%m-%Y") 
                    modelli = comune.modelli_f24_emessi
                    for modello in modelli: #Verifica che il modello per quella impresa non sia stato già emesso quest'anno
                        if modello.impresa.codice_fiscale == impresa.codice_fiscale and modello.impresa.denominazione == impresa.denominazione:
                            #Conversione in datetime per poterlo confrontare
                            if datetime.strptime(modello.data, "%d-%m-%Y").year < data_oggi.year: 
                                comune.emetti_modello_f24(impresa, data_oggi.strftime("%d-%m-%Y")) #Emetto il ModelloF24 con la data odierna
                                print("Modello F24 emesso. \n")
                                return
                            else: #Il modello è già stato emesso per l'anno in corso, il sistema chiede all'utente se vuole sovrascriverlo
                                answer = valida_dato(input("Il modello è già stato emesso quest'anno per l'impresa, vuoi sovrascriverlo? (S/N) "), "booleano", "Valore inserito non valido")
                                if answer == True: 
                                    modello = comune.emetti_modello_f24(impresa, data_oggi.strftime("%d-%m-%Y"))
                                    print("Il modello è stato sovrascritto. \n")
                                    return
                                else: 
                                    print("Il modello non è stato sovrascritto. \n")
                                    return
                    comune.emetti_modello_f24(impresa, data_oggi.strftime("%d-%m-%Y")) #Emetto il ModelloF24 con la data odierna
                    print("Modello F24 emesso. \n")
                    return
    print("L'impresa non è registrata a sistema. \n")
    
#Metodo che emette un ModelloF24 a ritroso per l'impresa

def emissione_modellof24_ritroso(lista_comuni):
    if len(lista_comuni) == 0: raise ValueError("Non sono presenti comuni registrati a sistema. ") #Verifica della presenza di comuni nell'array
    print("Inserisci i dati dell'azienda per l'emissione del Modello F24 in una data antecedente. \n")
    codice_fiscale = valida_dato(input("Quale è il codice fiscale dell'impresa? (11 cifre) "), "codice_fiscale", "Codice fiscale non valido")
    sede = input("Quale è la sede dell'impresa? ")
    if not sede[0].isupper():
        sede = sede.capitalize()
    for comune in lista_comuni:
        if comune.nome == sede:
            denominazione = input("Quale è il nome dell'impresa? ")
            if not denominazione[0].isupper(): 
                denominazione = denominazione.capitalize()
            stop = False
            while(stop == False):
                valori_ammessi = ["Societa per Azioni", "Societa Cooperativa", "Societa Responsabilita Limitata", "Impresa Individuale"]
                ragione_sociale = input(f"Quale è la ragione sociale dell'impresa? \nValori ammessi: {valori_ammessi}: ")
                if ragione_sociale not in valori_ammessi:
                    print("Valore non ammesso. \n")
                else: stop = True  
            divisione_ateco = input("Quale è la divisione ateco dell'impresa? ")
            if not divisione_ateco.isupper(): #Verifica che tutte le lettere siano maiuscole
                divisione_ateco = divisione_ateco.upper()
            numero_dipendenti = valida_dato(input("Quale è il numero di dipendenti dell'impresa? "), "intero", "Numero di dipendenti non valido")
            numero_soci = valida_dato(input("Quale è il numero di soci dell'impresa? "), "intero", "Numero di soci non valido")
            numero_amministratori = valida_dato(input("Quale è il numero di amministratori dell'impresa? "), "intero", "Numero di amministratori non valido")
            data_oggi = date.today() #Salvataggio della data odierna
            data_oggi = data_oggi.strftime("%d-%m-%Y") #Conversione in una stringa
            data_oggi = datetime.strptime(data_oggi, "%d-%m-%Y") #Conversione in datetime per poterlo confrontare
            stop = False
            while(stop == False):
                data_costituzione = valida_dato(input("Quale è la data di costituzione dell'impresa? (formato gg-mm-aaaa) "), "data", "Data di costituzione non valida")
                if datetime.strptime(data_costituzione) < data_oggi:
                    print("Data successiva alla data odierna. \n")
                    stop = True
            certificazioni_qualita = valida_dato(input("L'impresa ha certificazioni di qualità? (S/N) "), "booleano", "Valore inserito non valido")
            fatturato = valida_dato(input("Quale è il fatturato dell'impresa? (espresso in € e senza decimali) "), "intero", "Fatturato non valido")
            impresa = Impresa(codice_fiscale, denominazione, ragione_sociale, sede, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato)
            
            data = valida_dato(input("In che data del passato vuoi emettere il modello? (formato gg-mm-aaaa) "), "data", "Data non valida")
            if datetime.strptime(data, "%d-%m-%Y") < datetime.strptime(data_costituzione, "%d-%m-%Y"): print("Data antecedente alla data di costituzione dell'impresa. \n")
            elif data_oggi < datetime.strptime(data, "%d-%m-%Y"): print("Data successiva alla data odierna. \n")
            modelli = comune.modelli_f24_emessi
            for modello in modelli:
                if modello.impresa.codice_fiscale == impresa.codice_fiscale and modello.impresa.denominazione == impresa.denominazione:
                    if datetime.strptime(data, "%d-%m-%Y").year == datetime.strptime(modello.data, "%d-%m-%Y").year:
                        answer = valida_dato(input("Il modello è già stato emesso nell'anno indicato per l'impresa, vuoi sovrascriverlo? (S/N) "), "booleano", "Valore inserito non valido")
                        if answer == True: 
                            modello = comune.emetti_modello_f24(impresa, data)
                            print("Il modello è stato sovrascritto. \n")
                            return
                        else: 
                            print("Il modello non è stato sovrascritto. \n")
                            return
            comune.emetti_modello_f24(impresa, data) #Emissione del ModelloF24 con data nel passato
            print("Modello F24 emesso. \n")
            return
    print("Il comune della sede dell'impresa non è registrato a sistema. Per procedere registralo come nuovo comune. ")

#Metodo che stampa i ModelliF24 emessi per ogni comune

def stampa_modelliF24(lista_comuni):
    if len(lista_comuni) == 0: raise ValueError("Non sono presenti comuni registrati a sistema. ") #Verifica della presenza di comuni nell'array
    nome_comune = input("Di quale comune vuoi visualizzare i modelliF24? ")
    if not nome_comune[0].isupper(): 
        nome_comune = nome_comune.capitalize()
    for comune in lista_comuni:
        if comune.nome == nome_comune:
            if len(comune.modelli_f24_emessi) == 0:
                print(f"Per il comune {comune.nome} non esistono ModelliF24 emessi. ")
            print(f"Ecco la lista dei ModelliF24 emessi dal comune di {comune.nome}: ")
            for modello in comune.modelli_f24_emessi:
                print(f"\n{modello.prepara_f24()}\n") #Prepara_f24 restituisce un dizionario con i dati del modello
            return
    print("Il comune non è registrato a sistema. ")

#Metodo che restituisce un report con le statistiche sull'IRAP riscosso dal comune nel periodo

def genera_report(lista_comuni):
    if len(lista_comuni) == 0: raise ValueError("Non sono presenti comuni registrati a sistema. ") #Verifica della presenza di comuni nell'array
    nome_comune = input("Di quale comune vuoi visualizzare il report? ")
    if not nome_comune[0].isupper(): 
        nome_comune = nome_comune.capitalize()
    data_oggi = date.today() #Salvataggio della data odierna
    data_oggi = data_oggi.strftime("%d-%m-%Y") #Conversione in una stringa
    data_oggi = datetime.strptime(data_oggi, "%d-%m-%Y") #Conversione in datetime per poterlo confrontare
    stop = False #Inizializzazione di una variabile di cointrollo per la data
    while (stop == False):
        inizio = valida_dato(input("Inserisci una data di inizio periodo per l'emissione del report (formato gg-mm-aaaa): "), "data", "Data non valida")
        if data_oggi <  datetime.strptime(inizio, "%d-%m-%Y"): print("Data successiva alla data odierna ")
        else: stop = True
    stop = False
    while (stop == False):
        fine = valida_dato(input("Inserisci una data di fine periodo per l'emissione del report (formato gg-mm-aaaa): "), "data", "Data non valida")
        if data_oggi <  datetime.strptime(fine, "%d-%m-%Y"): print("Data successiva alla data odierna ")
        else: stop = True
    print(f"\nReport sull'IRAP riscosso dal comune di {nome_comune} dal {inizio} al {fine} \n")
    somma = 0
    conta = 0
    lista_imprese = []
    for comune in lista_comuni:
        if comune.nome == nome_comune:
            for modello in comune.modelli_f24_emessi: #Verifico che il modello sia stato rilasciato nel periodo indicato
                if datetime.strptime(modello.data, "%d-%m-%Y") <= datetime.strptime(fine, "%d-%m-%Y") and datetime.strptime(modello.data, "%d-%m-%Y") >= datetime.strptime(inizio, "%d-%m-%Y"): 
                    lista_imprese.append(modello.impresa)
                    somma += modello.importo_irap
                    conta += 1
            break
    if conta == 0: print(f"Nessun modelloF24 è stato rilasciato nell'intervallo indicato per il comune di {nome_comune} ")
    else: #Stampa delle statistiche
        print(f"Dati sulle imprese paganti dal comune di {comune.nome}. ")
        print(f"Numero di imprese paganti: {conta} ")
        print(f"Media del numero di Soci: {test_2.media_aritmetica(lista_imprese, 'numero_soci')} ")
        print(f"Media del numero di Amministratori: {test_2.media_aritmetica(lista_imprese, 'numero_amministratori')} ")
        print(f"Percentuale di qualità delle imprese: {test_2.quality_company(lista_imprese)} ")
        print(f"Società per Azioni con certificati di qualità: {test_2.quality_stocks(lista_imprese)} ")
        print(f"Numero di imprese per Divisione ATECO: {test_2.conta_aziende_per_ateco(lista_imprese)} \n")
        print(f"Dati sull'IRAP riscosso dal comune di {nome_comune}. ")
        print(f"Totale IRAP pagato nel periodo: {somma}€ ")
        print(f"Quota IRAP media per azienda nel periodo: {somma/conta}€ \n")