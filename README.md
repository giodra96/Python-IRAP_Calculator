# Come utilizzare IRAP-Calculator
## Prima parte: irap_management

In questa cartella è presente il programma principale che gestisce 

Entra nella cartella del progetto
```
$ cd irap_management
```
Crea il virtual enviroment
```
$ python3 -m venv .venv
```
Attiva il virtual enviroment:
- Linux/MacOS:
    ```
    $ source .venv/bin/activate
    ```
- Windows:
    ```
    $ .venv\Scripts\activate
    ```
    Se non è presente il comando ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```, esegui questo comando:
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    Esegui il comando:
    ```
    $ .venv\Scripts\activate
    ```
Installa le dipendenze
```
$ pip3 install -r requirements.txt
```
Infine, leggi il file Readme presente nella cartella per maggiori informazioni sull'utilizzo del programma.

# Come avviare il db
Entra nella cartella del progetto
```
$ cd db_integration
```
Crea i virtual enviroment
```
$ python3 -m venv .venv
```
Attiva il virtual enviroment:
- Linux/MacOS:
    ```
    $ source .venv/bin/activate
    ```
- Windows:
    ```
    $ .venv\Scripts\activate
    ```
    Se non è presente il comando ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```, esegui questo comando:
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    Esegui il comando:

    ```
    $ .venv\Scripts\activate
    ```
Installa le dipendenze
```
$ pip3 install -r requirements.txt
```
Avvia l'app
```
$ flask --app app run
```