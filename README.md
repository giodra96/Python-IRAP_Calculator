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

### **NB: Assicurarsi che il virtual environment sia stato attivato correttamente, altrimenti procedere alla selezione manuale**

4. **Installazione delle dipendenze:**

Utilizza **pip** per installare le dipendenze necessarie elencate nel file **requirements.txt**.
```
$ pip3 install -r requirements.txt
```
### **NB: Assicurarsi di essere all'interno della directory irap_management affinché il codice legga correttamente il file imprese.txt**

## Parte 2: db_integration

La cartella **db_integration** contiene una versione lite del programma per l'integrazione dei dati con il database.

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
Continua sul **Readme** di db_integration per consultare casi d'uso con dati pronti all'uso.