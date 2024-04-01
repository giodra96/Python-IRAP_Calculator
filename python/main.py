import test_2, test_3
from comune import Comune
from impresa import Impresa

# lettura file imprese
def creazione_comuni(lista_imprese):
    lista_comuni = []
    comunisegnati_visti = set()

    for impresa in lista_imprese:
        comunisegnati = impresa.sede_legale
        if comunisegnati not in comunisegnati_visti:
            comune = Comune(impresa.sede_legale)
            lista_comuni.append(comune)
            comunisegnati_visti.add(comunisegnati)
    
    assegna_imprese(lista_comuni, lista_imprese)

    return lista_comuni

def assegna_imprese(lista_comuni, lista_imprese):
    for  impresa in lista_imprese:
        for comune in lista_comuni:
            if impresa.sede_legale == comune.nome:
                if impresa not in comune.imprese_registrate:
                    comune.registra_impresa(impresa)

def main ():
    lista_imprese = test_2.lista_impreseordinate("imprese_ordinate.txt")
    lista_comuni = creazione_comuni(lista_imprese) #parto dai comuni già ppresenti nel file txt
    
    stop = False
    while (stop == False):
        value = input("Scegli un'opzione: \n 1: Aggiungi un nuovo comune  \n 2: Registra un'impresa presso il comune \n 3: Calcola IRAP per l'impresa \n 4: Emissione del modello F24 \n 5: Visualizza Modelli F24 per comune \n 6: Report IRAP \n 7: Esci \n")
        match value:
            case "1":
                lista_comuni = test_3.aggiungi_comune(lista_comuni)
            case "2":
                output = test_3.registra_impresa(lista_comuni, lista_imprese)
                lista_comuni = output["comuni"]
                lista_imprese = output["imprese"]
            case "3":
                print(test_3.calcola_irap(lista_imprese))
            case "4":
                test_3.emissione_modellof24(lista_comuni, lista_imprese)
            case "7":
                stop = True
    for impresa in lista_imprese:
        print(impresa.denominazione)

if __name__ == "__main__":
    main()