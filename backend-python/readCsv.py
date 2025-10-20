#importamos pandas para la manipulacion del csv
import pandas
import json

def validStructure(dataframe: pandas.DataFrame) -> int:
    columns = ["id","status","description"]
    
    # extraemos las columnas del dataFrame
    datacolumns = list(dataframe.columns)

    missingColumsn = [col for col in columns if col not in datacolumns]

    if missingColumsn:
        raise ValueError("Las siguientes columnas no se encuentran en el csv: ",missingColumsn)
    
    return True

def reportGenerate(dataframe: pandas.DataFrame,path:str):
    """
    Esta funcion genera un reporte en formato json desde dataframe
    """
    
    if not path.endswith(".json"):
        raise ValueError("La path debe corresponder a un archivo .json")
    
    validStructure(dataframe)
    report = {}

    report["Numero de entidades"] = totalEntities(dataframe)
    report["Numero de entidades activas"] = activeEntities(dataframe)
    report["Numero de entidades sin descripcion"] = entitiesWithoutDescription(dataframe)

    #se imprimen en consola los datos mas relevantes
    print(f"Total de entidades: {report['Numero de entidades']}")
    print(f"Entidades activas: {report['Numero de entidades activas']}")
    print(f"Entidades sin descripción: {report['Numero de entidades sin descripcion']}")
   

    with open(path,"w",encoding = "utf-8") as file:
        json.dump(report,file)

    print("reporte generado con exito en: ",path)

    return 0

def totalEntities(dataframe: pandas.DataFrame) -> int:
    """
    Esta función entrega el número de entidades del DataFrame
    Retorna -1 si el DataFrame es vacio o None
    """
    numEntities = -1
    if dataframe is None or dataframe.empty:
        return numEntities
    
    numEntities = int(len(dataframe))

    return numEntities

def activeEntities(dataframe: pandas.DataFrame) -> int:

    """
    Esta función busca la columan status y cuenta las entidades activas
    Retorna -1 si el dataframe es vacio o None
    """

    numEntities = -1
    if dataframe is None or dataframe.empty:
        return numEntities

    numEntities = dataframe[dataframe["status"] == "activo"].shape[0]

    
    return numEntities

def entitiesWithoutDescription(dataframe: pandas.DataFrame) -> int:

    numEntities = -1
    if dataframe is None or dataframe.empty:
        return numEntities

    numEntities = dataframe[dataframe["description"].isna()].shape[0]

    return numEntities

def validatePath(path:str) -> bool:
    import os

    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontro la path: {path}")
    if not path.endswith(".csv"):
        raise ValueError("El archivo tiene que terner extensión .csv")
    return True



if __name__ == "__main__":

    # path del archivo 
    path = 'items.csv'
    path_json = path[:-4]+"_report"+".json"

    # Validar la path 
    validatePath(path)


    # importamos la informacion desde el csv

    dataframe = pandas.read_csv(path)

   
    # generamos el reporte en un json estatico
    reportGenerate(dataframe,path_json)

    