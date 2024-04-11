# Come utilizzare irap_management
Entra nella cartella del progetto
```
$ cd irap_management
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