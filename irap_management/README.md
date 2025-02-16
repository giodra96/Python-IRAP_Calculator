# irap_management

Welcome to the program for calculating IRAP for businesses. Here you will find the description of the functionality and the steps for use.

## Description of classes

1. **Impresa** -> Class that defines the structure of a company through the following parameters:
    - codice_fiscale: string of length 11 that represents the company's tax code and must be unique
    - denominazione: string that represents the name of the company and must be unique
    - ragione_sociale: string that represents the company's legal form (Societa per Azioni, Societa Cooperativa, Societa Responsabilita Limitata, Impresa Individuale)
    - sede: string that represents the name of the municipality of the headquarters to which the company will have to pay the IRAP.
    - divisione_ateco: string that represents the code of the company's ATECO division
    - numero_dipendenti: integer that represents the number of employees of the company
    - numero_soci: integer that represents the number of members
    - numero_amministratori: integer that represents the number of administrators of the company
    - data_costituzione: represents the date of establishment of the company

    The class includes the following methods:
    - diritto_agevolazione(): verifies if the company is eligible for the reduced IRAP payment
    - calcola_irap(): calculates the company's IRAP

2. **Comune** -> Class that defines the structure of a municipality through the following parameters:
    - nome: string that represents the name of the municipality and must be unique
    - imprese_registrate: array containing the Impresa objects registered for the municipality
    - modelli_f24_emessi: array containing the ModelloF24 objects issued by the municipality

    The class includes the following methods:
    - registra_impresa(impresa): registers the Impresa object passed as a parameter in the imprese_registrate array
    - emetti_modello_f24(impresa, data): registers the ModelloF24 object passed as a parameter in the modelli_f24_emessi array for the date passed as a parameter

3. **ModelloF24** -> Class that defines the structure of an f24 form through the following parameters:
    - impresa: Impresa object that represents the company to which the F24 form belongs
    - data: date on which the f24 form was issued
    - importo_irap: integer calculated with the calcola_irap() method

    The class includes the following methods:
    - prepara_f24(): returns the ModelloF24

## Description of the tests

1. **test_1**

    This first test defines the following methods:

    - leggi_listaimprese(file_path): reads the companies from a .txt file and returns them in an array
    - dizionario(lista_imprese): creates a dictionary with the tax code as the key and the number of people involved as the value
    - ordina_imprese(lista_imprese): sorts the companies by ATECO division (ascending) and number of administrators (descending)
    - stampa_imprese(lista_imprese): prints the company information
    - scrivi_imprese(lista_imprese, file_path): writes the company information to a .txt file

2. **test_2**

    This second test defines the following methods:

    - media_aritmetica(lista_imprese, parametro): calculates the arithmetic mean over all companies for the parameter passed
    - quality_company(lista_imprese): returns the companies with quality certificates and with a turnover between 10,000 and 50,000
    - quality_stocks(lista_imprese): returns the companies with the legal form "Società per Azioni" and quality certifications
    - conta_aziende_per_ateco(lista_imprese): returns a dictionary with the ATECO code as the key and the relative number of companies as the value

3. **test_3**

    This third test defines the following methods:

    - valida_dato(valore, tipo_dato, messaggio_errore): verifies if the data passed is valid based on its type
    - aggiungi_comune(lista_comuni): allows the user to add a new municipality
    - registra_impresa(lista_comuni, lista_imprese): allows the user to register a new company
    - calcola_irap(lista_imprese): allows the user to calculate the IRAP for a company
    - emissione_modellof24(lista_comuni, lista_imprese): allows the user to issue an f24 form for a company
    - emissione_modellof24_ritroso(lista_comuni): allows the user to register an f24 form issued in the past
    - stampa_modelliF24(lista_comuni): allows the user to view the list of ModelliF24 issued for a municipality
    - genera_report(lista_comuni): allows the user to generate a report with information on the IRAP collected for a municipality

## Main

Finally, in the main function there are two methods:

- creazione_comuni(lista_imprese): registers Comune objects for all the locations of the companies imported from the .txt file
- assegna_imprese(lista_comuni, lista_imprese): registers the companies imported in the .txt file in their respective municipalities

From the main method it will then be possible to access all the functionalities of the program through a special switch.
