import os #permette di verificare l'esistenza del file imprese.txt
from impresa import Impresa
import pandas as pd

def lista_impreseordinate():
    lista_impreseordinate = []
    try: # Verifica l'esistenza del file imprese.txt
        with open("imprese_ordinate.txt", "r") as file: # Apertura del file imprese.txt per lettura
            for riga in file:
                dati_impresa = riga.split(",")
                impresa = Impresa(
                    dati_impresa[0],
                    dati_impresa[1],
                    dati_impresa[2],
                    dati_impresa[3],
                    dati_impresa[4],
                    int(dati_impresa[5]),
                    int(dati_impresa[6]),
                    int(dati_impresa[7]),
                    dati_impresa[8],
                    bool(dati_impresa[9].lower()=="true"),
                    int(dati_impresa[10])
                )
                lista_impreseordinate.append(impresa)

    except FileNotFoundError as fe: #catturo eventuale caso di errore
        print(fe)
    return lista_impreseordinate

def media_aritmetica(lista_imprese, parametro):
    
    somma = 0 # Variabile per la somma dei numeri di parametro
    for impresa in lista_imprese:
        somma += getattr(impresa, parametro)
    
        media = somma / len(lista_imprese)

    return {"La media aritmetica dei numeri di {parametro} è:": media}

def quality_company(lista_imprese):

    c = 0 # Variabile per la somma dei numeri di quality_company
    
    for impresa in lista_imprese:
            if impresa.certificazioni_qualita == True:
                c += 1
            elif impresa.fatturato >= 10000 and impresa.fatturato <= 50000:
                c += 1
    try:
        perc = (c / len(lista_imprese))*100
    except ZeroDivisionError as e:
        print(e)

    return {f"La percentuale di aziende di qualità è: {perc}%"}

def pandas(lista_imprese):
    df = pd.DataFrame([(impresa.denominazione, impresa.certificazioni_qualita, impresa.ragione_sociale) for impresa in lista_imprese],
                  columns=["Denominazione","Certificazioni di qualità", "Ragione Sociale"])
    
    aziende_filtrate = df[(df["Certificazioni di qualità"] == True) & (df["Ragione Sociale"] == "Societa per Azioni")]

    return aziende_filtrate["Denominazione"].to_string(index=False)

def conta_aziende_per_ateco(lista_imprese):
 
    divisioni_ateco = {}

    for impresa in lista_imprese:
        divisione_ateco = impresa.divisione_ateco 
        divisioni_ateco[divisione_ateco] = divisioni_ateco.get(divisione_ateco, 0) + 1

    result = []
    for divisione_ateco, numero_aziende in divisioni_ateco.items():
        print(f"{divisione_ateco}: {numero_aziende}")

def main():  # Funzione principale


    print(media_aritmetica(lista_impreseordinate(), 'numero_dipendenti'))
    print(media_aritmetica(lista_impreseordinate(), 'numero_soci'))

    print("\n")
    print(quality_company(lista_impreseordinate()))
    print("\n")

    print(pandas(lista_impreseordinate()))
    print("\n")

    print("A seguire il numero di aziende per ogni divisione ATECO: \n")
    conta_aziende_per_ateco(lista_impreseordinate())
    print("\n")

if __name__ == "__main__":
    main()

