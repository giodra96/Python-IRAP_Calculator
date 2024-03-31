import os #permette di verificare l'esistenza del file imprese.txt
from impresa import Impresa

def main():  # Funzione principale

    lista_imprese = []
    try: # Verifica l'esistenza del file imprese.txt
        with open("imprese.txt", "r") as file: # Apertura del file imprese.txt per lettura
            for riga in file:
                dati_impresa = riga.split(",")
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
                lista_imprese.append(impresa)

    except FileNotFoundError as fe: #catturo eventuale caso di errore
        print(fe)

    # Creazione del dizionario
    n_dipendenti = {} # Creazione del dizionario
    for impresa in lista_imprese:
        if impresa.codice_fiscale not in n_dipendenti: # Se il codice fiscale non è presente nel dizionario, aggiungo un elemento
            n_dipendenti[impresa.codice_fiscale] = [impresa, 0] # Aggiunta di un elemento al dizionario
        n_dipendenti[impresa.codice_fiscale][1] += impresa.numero_dipendenti + impresa.numero_soci + impresa.numero_amministratori 
      
    # Ordina lista_imprese per divisione_ateco e a parità di divisione_ateco per numero_amministratori 
    lista_imprese.sort(key=lambda x: (x.divisione_ateco, -x.numero_amministratori)) # Ordina la lista di oggetti Impresa per divisione_ateco e numero_amministratori in ordine decrescente.

    # Stampa dei dati di tutte le imprese presenti nella lista lista_imprese
    for impresa in lista_imprese:
        print(f"Codice fiscale: {impresa.codice_fiscale}, Denominazione: {impresa.denominazione}, Ragione sociale: {impresa.ragione_sociale}, Sede legale: {impresa.sede_legale}, Divisione ATECO: {impresa.divisione_ateco}, Numero dipendenti: {impresa.numero_dipendenti}, Numero soci: {impresa.numero_soci}, Numero amministratori: {impresa.numero_amministratori}, Data costituzione: {impresa.data_costituzione}, Certificazioni qualità: {impresa.certificazioni_qualita}, Fatturato: {impresa.fatturato} \n\n")
    
    # Creazione del file txt con la lista ordinata di lista_imprese per codice fiscale
    with open("imprese_ordinate.txt", "w") as file:
        for impresa in lista_imprese:
            file.write(f"{impresa.codice_fiscale},{impresa.denominazione},{impresa.ragione_sociale},{impresa.sede_legale},{impresa.divisione_ateco},{impresa.numero_dipendenti},{impresa.numero_soci},{impresa.numero_amministratori},{impresa.data_costituzione},{impresa.certificazioni_qualita},{impresa.fatturato}\n")

if __name__ == "__main__":
    main()
