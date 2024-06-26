#Il test_2 contiene metodi che si occupano principalmente di eseguire analisi e calcoli sull'array lista_imprese

import pandas as pd #Import della libreria pandas per la gestione dei dati

#Metodo che restituisce la media aritmetica su un parametro dell'array lista_imprese

def media_aritmetica(lista_imprese, parametro):
    somma = 0 
    for impresa in lista_imprese:
        somma += getattr(impresa, parametro) #Somma si incrementa con il paramertro dell'array lista_imprese passato in input
    try: #Verifica che la media aritmetica sia calcolabile
        media = somma / len(lista_imprese)
    except ZeroDivisionError as e: 
        print(e)
    return media

#Metodo che restituisce la percentuale di aziende che hanno certificati di qualità
#o che hanno fatturato compreso tra 10.000 e 50.000

def quality_company(lista_imprese):
    if len(lista_imprese) == 0: raise ValueError("Non sono presenti imprese. ") #Verifica della presenza di imprese nell'array
    c = 0 #Contatore delle quality_company
    for impresa in lista_imprese:
            if impresa.certificazioni_qualita == True:
                c += 1
            elif impresa.fatturato >= 10000 and impresa.fatturato <= 50000:
                c += 1
    if c!=0: #Verifica che la media aritmetica sia calcolabile
        perc = (c / len(lista_imprese))*100
        return str(perc) + "%"
    else: return str(0) + "%"

#Metodo che restituisce le aziende di qualità e che sono affiliate alla societa per azioni

def quality_stocks(lista_imprese):
    if len(lista_imprese) == 0: raise ValueError("Non sono presenti imprese. ") #Verifica della presenza di imprese nell'array
    df = pd.DataFrame([(impresa.denominazione, impresa.certificazioni_qualita, impresa.ragione_sociale) for impresa in lista_imprese],
                  columns=["Denominazione","Certificazioni di qualità", "Ragione Sociale"]) #Creo un DataFrame 
    #Filtro per le aziende di qualità e affiliate alla societa per azioni
    aziende_filtrate = df[(df["Certificazioni di qualità"] == True) & (df["Ragione Sociale"] == "Societa per Azioni")] 
    return aziende_filtrate["Denominazione"].to_string(index=False)

#Metoto che restituisce per ogni divisione ATECO il corrispettivo numero di aziende

def conta_aziende_per_ateco(lista_imprese):
    if len(lista_imprese) == 0: raise ValueError("Non sono presenti imprese. ") #Verifica della presenza di imprese nell'array
    divisioni_ateco = {} #Creazione di un dizionario vuoto
    for impresa in lista_imprese:
        divisione_ateco = impresa.divisione_ateco #Salvo il valore di divisione ATECO
        divisioni_ateco[divisione_ateco] = divisioni_ateco.get(divisione_ateco, 0) + 1 #Incremento il valore della specifica divisione ATECO nel dizionario
    return divisioni_ateco

