#Il test_1 contiene metodi il cui scopo principale è la creazione e gestione di un array di oggetti Impresa

from impresa import Impresa #Import della classe Impresa dal file impresa.py

#Metodo che legge le imprese presenti su un file.txt passato come parametro
#e per ogni impresa crea un oggetto Impresa aggiungendolo all'array lista_imprese

def leggi_listaimprese(file_path):
    lista_imprese = [] #Inizializzo l'array lista_imprese
    try: #Verifica l'esistenza del file.txt
        with open(file_path, "r") as file: #Apertura del file.txt passato come parametro
            for riga in file:
                dati_impresa = riga.split(",") #Definisco il tipo di separatore
                impresa = Impresa(
                    dati_impresa[0],
                    dati_impresa[1],
                    dati_impresa[2],
                    dati_impresa[3],
                    dati_impresa[4],
                    int(dati_impresa[5]),
                    int(dati_impresa[6]),
                    int(dati_impresa[7]),
                    dati_impresa[8],
                    bool(dati_impresa[9].lower()=="true"),
                    int(dati_impresa[10])
                )
                stop = False #Inizializzazione di una variabile di controllo
                for impresa2 in lista_imprese: #Verifica che non esistono imprese già registrate con lo stesso codice fiscale e denominazione
                    if impresa2.codice_fiscale == impresa.codice_fiscale and impresa2.denominazione == impresa.denominazione:
                        stop = True
                if stop == False:
                    lista_imprese.append(impresa) #Aggiungo l'oggetto Impresa all'array lista_imprese
    except FileNotFoundError as fe: #Catturo eventuale caso di errore
        print(fe)
    return lista_imprese

#Metodo che crea un dizionario che associa ad ogni codice fiscale il numero di persone coinvolte nell'impresa

def dizionario(lista_imprese):
    if len(lista_imprese) == 0: raise ValueError("Non sono presenti imprese. ") #Verifica della presenza di imprese nell'array
    #Creazione del dizionario
    n_dipendenti = {} #Creazione del dizionario
    for impresa in lista_imprese:
        if impresa.codice_fiscale not in n_dipendenti: #Se il codice fiscale non è presente nel dizionario, aggiungo un elemento
            n_dipendenti[impresa.codice_fiscale] = 0 #Aggiunta di un elemento al dizionario
        n_dipendenti[impresa.codice_fiscale] += impresa.numero_dipendenti + impresa.numero_soci + impresa.numero_amministratori 
    return n_dipendenti

#Metodo che ordina lista_imprese per divisione_ateco (in ordine crescente) e a parità di divisione_ateco per numero_amministratori (in ordine decrescente)

def ordina_imprese(lista_imprese):
    lista_imprese.sort(key=lambda x: (x.divisione_ateco, -x.numero_amministratori)) 
    return lista_imprese

#Metodo che stampa dei dati di tutte le imprese presenti nella lista lista_imprese

def stampa_imprese(lista_imprese):
    for impresa in lista_imprese:
        print(f"Codice fiscale: {impresa.codice_fiscale}, Denominazione: {impresa.denominazione}, Ragione sociale: {impresa.ragione_sociale}, Sede: {impresa.sede}, Divisione ATECO: {impresa.divisione_ateco}, Numero dipendenti: {impresa.numero_dipendenti}, Numero soci: {impresa.numero_soci}, Numero amministratori: {impresa.numero_amministratori}, Data costituzione: {impresa.data_costituzione}, Certificazioni qualità: {impresa.certificazioni_qualita}, Fatturato: {impresa.fatturato} \n")

#Metodo che scrive su file.txt tutte le imprese presenti nella lista lista_imprese

def scrivi_imprese(lista_imprese, file_path):
    with open(file_path, "w") as file:
        for impresa in lista_imprese:
            file.write(f"{impresa.codice_fiscale},{impresa.denominazione},{impresa.ragione_sociale},{impresa.sede},{impresa.divisione_ateco},{impresa.numero_dipendenti},{impresa.numero_soci},{impresa.numero_amministratori},{impresa.data_costituzione},{impresa.certificazioni_qualita},{impresa.fatturato}\n")