# DB Flask

## Step per l'utilizzo del db

1. Installa e/o avvia postman per l'utilizzo delle API REST create in flask

2. Entra nel workspace e crea una nuova richihesta da file > new > http

3. Scegli il metodo desiderato  (GET, POST, PUT, DELETE) e inserisci l'url della risorsa che vuoi utilizzare (**vedi casi d'uso sotto**)

4. Inserisci i dati nel body se necessario (**alcuni esempi di body sono presenti nei casi d'uso sotto**)

5. Invia la richihesta e visualizza la risposta

## Casi d'uso

**Disclaimer**
I seguenti casi d'uso sono stati disposti nell'ordine esatto per il test di tutte le API REST create. 
Se non eseguite in questo ordine potrebbe essere necessaria una loro diversa configurazione per il corretto funzionamento del programma.
Vedi note aggiuntive su come configurare le API.

### Creazione di un nuovo comune

Milano:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/comuni
- **Body**: {"nome": "Milano"}

Cosenza:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/comuni
- **Body**: {"nome": "Cosenza"}

Roma:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/comuni
- **Body**: {"nome": "Roma"}

**Note**: i comuni vengono creati con un id crescente, tenere in considerazione l'id corretto per l'uso delle successive API dove richiesto.

### Visualizzazione di tutti i comuni

- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/comuni

### Modifica del comune Cosenza in Torino

- **Metodo**: PUT
- **URL**: http://127.0.0.1:5000/api/comuni/2
- **Body**: {"nome": "Cosenza"}

**Note**: Cosenza è associata all'id 2, per la modifica di un comune generico è necessario modificare l'id del comune nell'url.

### Visualizzazione del comune di Torino

- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/comuni/2

**Note**: Torino è associata all'id 2, per la visualizzazione di un comune generico è necessario modificare l'id del comune nell'url.

### Eliminazione del comune di Roma
- **Metodo**: DELETE
- **URL**: http://127.0.0.1:5000/api/comuni/3

**Note**: Roma è associata all'id 3, per l'eliminazione di un comune generico è necessario modificare l'id del comune nell'url.

### Creazione di una nuova impresa

Nexi:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/imprese
- **Body**: {"codice_fiscale": "09489670969",
            "denominazione": "Nexi",
            "ragione_sociale": "Societa per Azioni",
            "sede": "Milano",
            "divisione_ateco": "K64",
            "numero_dipendenti": 102,
            "numero_soci": 8,
            "numero_amministratori": 13,
            "data_costituzione": "10-11-2017",
            "certificazioni_qualita": true,
            "fatturato": 3260000000,
            "comune_id": 1}

Will:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/imprese
- **Body**: {"codice_fiscale": "04346220967",
            "denominazione": "Will",
            "ragione_sociale": "Società Responsabilita Limitata",
            "sede": "Milano",
            "divisione_ateco": "J58",
            "numero_dipendenti": 10,
            "numero_soci": 2,
            "numero_amministratori": 1,
            "data_costituzione": "17-06-2020",
            "certificazioni_qualita": true,
            "fatturato": 4600000,
            "comune_id": 1}

Directa:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/imprese
- **Body**: {"codice_fiscale": "06131300722",
            "denominazione": "Directa",
            "ragione_sociale": "Società Responsabilita Limitata",
            "sede": "Torino",
            "divisione_ateco": "K64",
            "numero_dipendenti": 12,
            "numero_soci": 3,
            "numero_amministratori": 2,
            "data_costituzione": "13-05-1962",
            "certificazioni_qualita": true,
            "fatturato": 22960000,
            "comune_id": 2}

Young Platform:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/imprese
- **Body**: {"codice_fiscale": "11931440017",
            "denominazione": "Young Platform",
            "ragione_sociale": "Societa per Azioni",
            "sede": "Torino",
            "divisione_ateco": "K64",
            "numero_dipendenti": 60,
            "numero_soci": 6,
            "numero_amministratori": 8,
            "data_costituzione": "07-02-2015",
            "certificazioni_qualita": true,
            "fatturato": 1605000,
            "comune_id": 2}

**Note**: le impprese vengono create con un id crescente, tenere in considerazione l'id corretto per l'uso delle successive API dove richiesto. L'id comune è associato al comune di riferimento, per la creazione di una nuova impresa è necessario modificare il comune nell'url.

### Visualizzazione di tutte le imprese
- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/imprese

### Modifica delle certificazioni di qualità di Will in false

- **Metodo**: PUT
- **URL**: http://127.0.0.1:5000/api/imprese/2
- **Body**: {"codice_fiscale": "04346220967",
            "denominazione": "Will",
            "ragione_sociale": "Società Responsabilita Limitata",
            "sede": "Milano",
            "divisione_ateco": "J58",
            "numero_dipendenti": 10,
            "numero_soci": 2,
            "numero_amministratori": 1,
            "data_costituzione": "17-06-2020",
            "certificazioni_qualita": false,
            "fatturato": 4600000,
            "comune_id": 1}

**Note**: per le modifiche indicare nell'url l'id corretto dell'impresa da modificare.

### Visualizzazione dell'impresa con le modifiche effettuate
- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/imprese/2

**Note**: per visualizzare l'impresa indicare nell'url l'id corretto.

### Eliminazione dell'impresa Young Platform
- **Metodo**: DELETE
- **URL**: http://127.0.0.1:5000/api/imprese/4

**Note**: per eliminare l'impresa indicare nell'url l'id corretto.

### Creazione ModelloF24

Nexi su Milano:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/modellif24
- **Body**: {"impresa_id": 1,
            "comune_id": 1,
            "data": "02-03-2024"}

Will su Milano:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/modellif24
- **Body**: {"impresa_id": 2,
            "comune_id": 1,
            "data": "10-02-2024"}

Directa su Torino:
- **Metodo**: POST
- **URL**: http://127.0.0.1:5000/api/modellif24
- **Body**: {"impresa_id": 3,
            "comune_id": 2,
            "data": "17-02-2024"}

**Note**: per creare il modellof24 indicare l'id dell'impresa e del comune corretto.

### Visualizzazione di tutti i ModelloF24
- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/modellif24

### Cambiamo la data del modello 
- **Metodo**: PUT
- **URL**: http://127.0.0.1:5000/api/modellif24/3
- **Body**: {"data": "20-02-2024"}

**Note**: per modificare il modellof24 indicare l'id del modello nell'url.

### Visualizzazione delle modifiche effettuate sul modello
- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/modellif24/3

**Note**: per visualizzare il modellof24 indicare l'id del modello nell'url.

### Eliminazione di un modello
- **Metodo**: DELETE
- **URL**: http://127.0.0.1:5000/api/modellif24/3

**Note**: per eliminare il modellof24 indicare l'id del modello nell'url.

### Stampa del modelloF24
- **Metodo**: GET
- **URL**: http://127.0.0.1:5000/api/modellif24/1/prepara

**Note**: per preparare e stampare il modellof24 indicare l'id del modello nell'url.
