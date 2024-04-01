from comune import Comune
from datetime import datetime, date
from impresa import Impresa

def valida_dato(valore, tipo_dato, messaggio_errore):
    try:
        if tipo_dato == "intero":
            if valore < 1:
                raise ValueError("Numero non valido")
            return int(valore)
        elif tipo_dato == "data":
            datetime.strptime(valore, "%d-%m-%Y")
            return valore
        elif tipo_dato == "booleano":
            return bool(valore.lower() in ["true", "si"])
        elif tipo_dato == "codice_fiscale":
            if len(str(valore)) != 11:
                raise ValueError("Codice fiscale non valido")
            return int(valore)
    except ValueError:
        raise ValueError(messaggio_errore)

def aggiungi_comune(lista_comuni):
    stop = False

    while(stop == False):
        stop2 = False

        while(stop2 == False):
            stop2 = True
            nome = input("Quale è il nome del comune? ")

            for comune in lista_comuni:
                if nome == comune.nome: 
                    print("Il comune è già presente")
                    stop2 = False
                    break
            
        comune = Comune(nome)
        lista_comuni.append(comune) #aggiungo il nuovo comune alla lista
        stop = input("Vuoi inserire altri comuni? (S/N): ") in ["n", "N"]

    return lista_comuni

def registra_impresa(lista_comuni, lista_imprese):
    stop = False
    codice_fiscale = valida_dato(input("Quale è il codice fiscale dell'impresa? "), "codice_fiscale", "Codice fiscale non valido")

    for impresa in lista_imprese:
        if impresa.codice_fiscale == codice_fiscale:
            print("Impresa già registrata")
            stop = True
            break

    if (stop == False):
        sede_legale = input("Quale è la sede legale dell'impresa? ")
        for comune in lista_comuni:
            if comune.nome == sede_legale:
                denominazione = input("Quale è il nome dell'impresa? ")
                ragione_sociale = input("Quale è la ragione sociale dell'impresa? ")
                divisione_ateco = input("Quale è la divisione ateco dell'impresa? ")
                numero_dipendenti = valida_dato(input("Quale è il numero di dipendenti dell'impresa? "), "intero", "Numero di dipendenti non valido")
                numero_soci = valida_dato(input("Quale è il numero di soci dell'impresa? "), "intero", "Numero di soci non valido")
                numero_amministratori = valida_dato(input("Quale è il numero di amministratori dell'impresa? "), "intero", "Numero di amministratori non valido")
                data_costituzione = valida_dato(input("Quale è la data di costituzione dell'impresa? "), "data", "Data di costituzione non valida")
                certificazioni_qualita = valida_dato(input("L'impresa ha certificazioni di qualità? "), "booleano", "Certificazioni di qualità non valide")
                fatturato = valida_dato(input("Quale è il fatturato dell'impresa? "), "intero", "Fatturato non valido")
                impresa = Impresa(codice_fiscale, denominazione, ragione_sociale, sede_legale, divisione_ateco, numero_dipendenti, numero_soci, numero_amministratori, data_costituzione, certificazioni_qualita, fatturato)
                comune.registra_impresa(impresa)
                lista_imprese.append(impresa)
                break
        
        print(f"Comune {sede_legale} non presente nella lista dei comuni")

    return {"imprese": lista_imprese, "comuni": lista_comuni}

def calcola_irap (lista_imprese):
    stop = False
    nome = input("Di quale azienda vuoi calcolare l'IRAP? ")
    for impresa in lista_imprese:
        if nome == impresa.denominazione:
            totale_irap = impresa.calcola_irap()
            stop = True
            break

    if stop != False:
        return totale_irap
    else: return "L'impresa non è registrata a sistema"

def emissione_modellof24(lista_comuni, lista_imprese):
    stop = False
    nome = input("Di quale azienda vuoi emettere il modelloF24? ")
    for impresa in lista_imprese:
        if nome == impresa.denominazione:
            for comune in lista_comuni:
                if comune.nome == impresa.sede_legale:
                    comune.emetti_modello_f24(impresa, date.today())
                    print("Modello F24 emesso")
                    stop = True
                    break
        if stop == True: break
    if stop == False: print("L'impresa non è registrata a sistema")

