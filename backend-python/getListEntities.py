import pandas

def getListEntities(entities:list)-> list:

    # casos limite
    if not entities: 
        raise ValueError("La lista esta vacía")
    # Si la lista tiene menos de 3 elementos 
    if len(entities)<3:
        raise ValueError("La lista debe de contener a lo menos 3 elementos")
    

    orderList=sorted(entities
        ,key=lambda item: len(item.get("description")) if item.get("description") is not None else 0 # manejo de nulls
        ,reverse=True )
   
    entitiesList = orderList[:3]

    return entitiesList


if __name__ == "__main__":

    # supondremos que la lista de entities es de la sigueinte forma 
    entitiesList = [
  {
    "id": 1,
    "name": "Sombrilla de playa",
    "description": "Sombrilla grande",
    "status": "activo",
    "created_at": "2025-01-15T10:30:00"
  },
  {
    "id": 2,
    "name": "Toalla de playa",
    "description": "Toalla de microfibra",
    "status": "activo",
    "created_at": "2025-01-16T14:20:00"
  },
  {
    "id": 3,
    "name": "Protector solar",
    "description": "Protector solar resistente al agua",
    "status": "inactivo",
    "created_at": "2025-01-17T09:15:00"
  },
  {
    "id": 4,
    "name": "Pelota de playa",
    "description": "Pelota inflable",
    "status": "activo",
    "created_at": "2025-01-18T16:45:00"
  },
  {
    "id": 5,
    "name": "Gafas de sol",
    "description": "lentes para proteccion contra el sol",
    "status": "activo",
    "created_at": "2025-01-19T11:30:00"
  },
  {
    "id": 6,
    "name": "Gorra de playa",
    "description": None,
    "status": "inactivo",
    "created_at": "2025-01-19T15:30:00"
  },
  {
    "id": 7,
    "name": "Sandalias de playa",
    "description": None,
    "status": "activo",
    "created_at": "2025-01-19T18:30:00"
  }
]

    entities = getListEntities(entitiesList)
    print("Las 3 principales entidades son : ",entities)