# irapp_management

Benvenuti nel programma pper il calcolo dell'IRAP per le imprerse. Qui troverete la descrizione della funzionalità e i passaggi per l'utilizzo.

## Descrizione delle classi

1. **Impresa** -> Classe che definisce la struttura di un impresa attraverso i seguenti parametri:
    - codice_fiscale: stringa di lunghezza 11 che rappresenta il codice fiscale dell'impresa e deve essere univoca
    - denominazione: stringa che rappresenta il nome dell'impresa e deve essere univoco
    - ragione_sociale: stringa che rappresenta la ragione sociale dell'impresa (Societa per Azioni, Societa Cooperativa, Societa Responsabilita Limitata, Impresa Individuale)
    - sede: stringa che rappresenta il nome del comune della sede al quale l'impresa dovrà pagare l'IRAP.
    - divisione_ateco: stringa che rappresenta il codice della divisione ateco dell'impresa
    - numero_dipendenti: intero chhe rappresenta il numero di dipendenti dell'impresa
    - numero_soci: intero che rappresenta il numero di soci
    - numero_amministratori: intero che rappresenta il numero di amministratori dell'impresa
    - data_costituzione: rappresenta la data di costituzione dell'impresa

    La classe comprende i seguenti metodi:
    - diritto_agevolazione(): verifica se l'impresa rientra nel pagamento dell'IRAP agevolato
    - calcola_irap(): calcola l'IRAP dell'impresa

2. **Comune** -> Classe che definisce la struttura di un comune attraverso i seguenti parametri:
    - nome: stringa che rappresenta il nome del comune e deve essere univoca
    - imprese_registrate: array contenente gli oggetti Impresa registrati per il comune
    - modelli_f24_emessi: array contenente gli oggetti ModelloF24 emessi dal comune

    La classe comprende i seguenti metodi:
    - registra_impresa(impresa): registra l'oggetto Impresa passato come parametro nell'array imprese_registrate
    - emetti_modello_f24(impresa, data): registra l'oggetto ModelloF24 passato come parametro nell'array modelli_f24_emessi per la data passata come parametro

3. **ModelloF24** -> Classe che definisce la struttura di un modello f24 attraverso i seguenti parametri:
    - impresa: oggetto Impresa che rappresenta l'impresa a cui appartiene il modello F24
    - data: data in cui è stato emesso il modello f24
    - importo_irap: intero calcolato con il metodo calcola_irap()

    La classe comprende i seguenti metodi:
    - prepara_f24(): restituisce il modelloF24 

## Descrizione dei test

1. test_1

    Questo primo test definisce i seguenti metodi:

    - leggi_listaimprese(file_path): legge le impresse da un file.txt e le restituisce in un array
    - dizionario(lista_imprese): crea un dizionario con il codice fiscale come chiave e il numero di persone coinvolte come valore
    - ordina_imprese(lista_imprese): ordina le imprese per divisione ateco (crescente) e numero amministratori (decrescente)
    - stampa_imprese(lista_imprese): stampa le informazioni delle imprese 
    - scrivi_imprese(lista_imprese, file_path): scrive le informazioni delle imprese in un file.txt

2. test_2

    Questo secondo test definisce i seguenti metodi:

    - media_aritmetica(lista_imprese, parametro): calcola la media aritmetica su tutte le imprese per il parametro passato
    - quality_company(lista_imprese): restituisce le imprese con certificati di qualità e con un fatturato compreso tra 10.000 e 50.000
    - quality_stocks(lista_imprese): restituisce le imprese con ragione sociale "Società per Azioni" e certificazioni di qualità
    - conta_aziende_per_ateco(lista_imprese): restituisce un dizionario con il codice ateco come chiave e il relativo numero di aziende come valore

3. test_3

    Questo terzo test definisce i seguenti metodi:

    - valida_dato(valore, tipo_dato, messaggio_errore): verifica se il dato passato è valido sulla base del suo tipo
    - aggiungi_comune(lista_comuni): permette all'utente di aggiungere un nuovo comune 
    - registra_impresa(lista_comuni, lista_imprese): permette all'utente di registrare una nuova impresa
    - calcola_irap(lista_imprese): permette all'utente di calcolare l'IRAP per un'impresa
    - emissione_modellof24(lista_comuni, lista_imprese): permette all'utente di emettere un modello f24 per un'impresa
    - emissione_modellof24_ritroso(lista_comuni): permette all'utente di registrarte a sistema un modello f24 emesso nel passato
    - stampa_modelliF24(lista_comuni): permette all'utente di visualizzare la lista di modelliF24 emessi per un comune
    - genera_report(lista_comuni): permette all'utente di generare un report con le informazioni sull'IRAP riscossa per un comune

## Main

Infine, nella funzione main sono presenti due metodi:

- creazione_comuni(lista_imprese): registra a sistema oggetti Comune per tutte le sedi delle imprese importate dal file .txt
- assegna_imprese(lista_comuni, lista_imprese): registra le imprese importate nel file .txt nei rispettivi comuni 

Dal metodo main sarà poi possibile accedere a tutte le funzionalità del programma attraverso un'apposito switch.