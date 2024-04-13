import test_1, test_3 #Importo i test 2 e 3 per poterli utilizzare nel main
from comune import Comune #Importo la classe Comune

#Metodo per la creazione dei comuni presenti (come attributo sede legale di un oggetto Impresa) in una lista di imprese

def creazione_comuni(lista_imprese):
    lista_comuni = [] #Creazione di una lista vuota per i comuni
    comunisegnati_visti = set() #Creazione di un set vuoto per i comuni già presenti
    for impresa in lista_imprese:
        comunisegnati = impresa.sede_legale
        if comunisegnati not in comunisegnati_visti: #Se il comune non è già presente allora lo aggiungo
            comune = Comune(impresa.sede_legale) #Creazione di un comune con il nome del comune
            lista_comuni.append(comune)
            comunisegnati_visti.add(comunisegnati) #Aggiungo il comune all'interno del set
    assegna_imprese(lista_comuni, lista_imprese) #Assegno le imprese alle loro comuni
    return lista_comuni

#Metodo per la registrazione di una lista di imprese ai relativi comuni

def assegna_imprese(lista_comuni, lista_imprese):
    for  impresa in lista_imprese:
        for comune in lista_comuni:
            if impresa.sede_legale == comune.nome:
                if impresa not in comune.imprese_registrate: #Se l'impresa non è già registrata allora la registro
                    comune.registra_impresa(impresa)

#Metodo principale

def main ():
    lista_imprese = test_1.leggi_listaimprese("C:\\Users\\Giodra\\Desktop\\Master\\MasterAI\\irap_management\\imprese.txt") #Lettura delle imprese da un file.txt
    lista_imprese = test_1.ordina_imprese(lista_imprese) #Ordinamento le imprese
    test_1.scrivi_imprese(lista_imprese, "imprese_ordinate.txt") #Scrittura delle imprese ordinate in un file.txt
    print("Imprese presenti a sistema: \n")
    test_1.stampa_imprese(lista_imprese) #Stampa delle imprese
    print(f"\nNumero totale delle persone coinvolte per ogni impresa {test_1.dizionario(lista_imprese)} \n") #Stampo il numero totale delle persone coinvolte per ogni impresa
    lista_comuni = creazione_comuni(lista_imprese) #Creazione dei comuni a partire dalle imprese importate dal file.txt
    stop = False #Creazione di una variabile di controllo per la chiusura della chiamata del menu
    while (stop == False):
        value = input("Scegli un'opzione: \n 1: Aggiungi un nuovo comune  \n 2: Registra un'impresa presso il comune \n 3: Calcola IRAP per l'impresa \n 4: Emissione del modelloF24 per un'impresa \n 5: Emissione del modelloF24 a ritroso per un'impresa \n 6: Visualizza Modelli F24 per comune \n 7: Report IRAP \n 8: Esci \n")
        match value:
            case "1": #Aggiunta di un nuovo comune
                lista_comuni = test_3.aggiungi_comune(lista_comuni)
            case "2": #Registrazione di un'impresa presso il comune corrispondente
                output = test_3.registra_impresa(lista_comuni, lista_imprese)
                lista_comuni = output["comuni"] #Aggiorno le liste dei comuni e delle imprese
                lista_imprese = output["imprese"]
            case "3": #Calcolo IRAP per l'impresa
                print(f"{test_3.calcola_irap(lista_imprese)} \n")
            case "4": #Emissione del modello F24 per un'impresa
                test_3.emissione_modellof24(lista_comuni, lista_imprese)
            case "5": #Emissione del modello F24 a ritroso per un'impresa
                test_3.emissione_modellof24_ritroso(lista_comuni)
            case "6": #Stampa dei modelliF24 per ogni comune della lista
                test_3.stampa_modelliF24(lista_comuni) 
            case "7": #Report IRAP per il comune
                test_3.genera_report(lista_comuni)
            case "8":
                stop = True
            case _: #Caso default
                print("Scelta non valida")

if __name__ == "__main__":
    main()