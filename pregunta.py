"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", encoding="utf-8", index_col=0)
    
    df = df.dropna(axis=0)
    for col in df.columns:
        if (df[col].dtype not in ['int64', 'float64']):
            df[col] = df[col].apply(str.lower)            
            df[col] = df[col].apply(lambda x: x.replace("_", " "))
            df[col] = df[col].apply(lambda x: x.replace("-", " "))
            df[col] = df[col].apply(lambda x: x.replace("$", ""))
            df[col] = df[col].apply(lambda x: x.replace("$ ", ""))
            df[col] = df[col].apply(lambda x: x.replace(".00", ""))
            df[col] = df[col].apply(lambda x: x.replace(",", ""))
        if (col == "comuna_ciudadano"):
            df[col] = df[col].apply(lambda x: float(x))
        if (col == "monto_del_credito"):
            df[col] = df[col].apply(lambda x: int(x))
        if (col == "fecha_de_beneficio"):
            df[col] = df[col].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/",x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    df = df.drop_duplicates().reset_index(drop=True)       
    return df
