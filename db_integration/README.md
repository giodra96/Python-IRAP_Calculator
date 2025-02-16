# DB Flask

## Steps for using the database

1. Install and/or start Postman to use the REST APIs created in Flask.

2. Enter the workspace and create a new request from File > New > HTTP.

3. Choose the desired method (GET, POST, PUT, DELETE) and enter the URL of the resource you want to use (**see use cases below**).

4. Enter the data in the body if necessary (**some examples of bodies are present in the use cases below**).

5. Send the request and view the response.

## Use Cases

**Disclaimer**
The following use cases have been arranged in the exact order for testing all the created REST APIs.
If not executed in this order, their different configuration may be necessary for the correct functioning of the program.
See additional notes on how to configure the APIs.

### Creating a new comune

Milan:
- **Method**: POST
- **URL**: http://127.0.0.1:5000/api/comuni
- **Body**: {"nome": "Milano"}

Cosenza:
- **Method**: POST
- **URL**: http://127.0.0.1:5000/api/comuni
- **Body**: {"nome": "Cosenza"}

Rome:
- **Method**: POST
- **URL**: http://127.0.0.1:5000/api/comuni
- **Body**: {"nome": "Roma"}

**Note**: i comuni are created with an incrementing id, take into account the correct id for the use of subsequent APIs where required.

### Viewing all comuni

- **Method**: GET
- **URL**: http://127.0.0.1:5000/api/comuni

### Modifying the comune Cosenza to Torino

- **Method**: PUT
- **URL**: http://127.0.0.1:5000/api/comuni/2
- **Body**: {"nome": "Torino"}

**Note**: Cosenza is associated with id 2, for modifying a generic comune it is necessary to modify the comune id in the URL.

### Viewing the comune of Torino

- **Method**: GET
- **URL**: http://127.0.0.1:5000/api/comuni/2

**Note**: Torino is associated with id 2, for viewing a generic comune it is necessary to modify the comune id in the URL.

### Deleting the comune of Rome
- **Method**: DELETE
- **URL**: http://127.0.0.1:5000/api/comuni/3

**Note**: Roma is associated with id 3, for deleting a generic comune it is necessary to modify the comune id in the URL.

### Creating a new impresa

Nexi:
- **Method**: POST
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
- **Method**: POST
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
- **Method**: POST
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
- **Method**: POST
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

**Note**: le imprese are created with an incrementing id, take into account the correct id for the use of subsequent APIs where required. The comune id is associated with
