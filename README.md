# Come avviare il backend
Entra nella cartella del progetto
```
$ cd backend
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