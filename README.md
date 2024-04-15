# Come utilizzare IRAP-Calculator
## Parte 1: irap_management

La cartella **irap_management** contiene il programma principale per gestire il calcolo dell'IRAP per le imprese.

Per comprendere appieno il funzionamento del programma e imparare come utilizzarlo, consulta il file **Readme** associato.

### Avvio del programma

Segui questi passaggi per avviare il programma:

1. **Naviga nella cartella del progetto:**
```
$ cd irap_management
```
2. **Crea un ambiente virtuale:**

Utilizza il modulo **venv** per creare un ambiente virtuale isolato per il progetto.
```
$ python3 -m venv .venv
```
3. **Attiva il virtual enviroment:**

    - Linux/MacOS:
    ```
    $ source .venv/bin/activate
    ```
    - Windows:
    ```
    $ .venv\Scripts\activate
    ```
    Se il comando non funziona, potrebbe essere necessario eseguire il seguente comando prima:
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    Quindi, esegui di nuovo il comando per attivare l'ambiente virtuale:
    ```
    $ .venv\Scripts\activate
    ```
4. **Installazione delle dipendenze:**

Utilizza **pip** per installare le dipendenze necessarie elencate nel file **requirements.txt**.
```
$ pip3 install -r requirements.txt
```

## Parte 2: db_integration

Per comprendere appieno il funzionamento del programma e imparare come utilizzarlo, consulta il file **Readme** associato.

### Avvio del programma

Segui questi passaggi per avviare il programma:

1. **Naviga nella cartella del progetto:**
```
$ cd db_integration
```
2. **Crea il virtual environment e installa le dipendenze come spiegato sopra**

3. **Avvia flask**
```
$ flask --app app run
```