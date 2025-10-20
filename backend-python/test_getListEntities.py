import pytest
from getListEntities import getListEntities


# Fixture de datos para reutilizar la lista de prueba
@pytest.fixture
def originalEntitiesList():
    """Retorna la lista de las entidadesa usar para los test"""
    return [
        {"id": 1, "name": "Sombrilla", "description": "Sombrilla grande", "status": "activo"},
        {"id": 2, "name": "Toalla", "description": "Toalla de microfibra", "status": "activo"},
        {"id": 3, "name": "Protector", "description": "Protector solar resistente al agua", "status": "inactivo"},
        {"id": 4, "name": "Pelota", "description": "Pelota inflable", "status": "activo"},
        {"id": 5, "name": "Gafas", "description": "lentes para proteccion contra el sol", "status": "activo"},
        {"id": 6, "name": "Gorra", "description": None, "status": "inactivo"},
        {"id": 7, "name": "Sandalias", "description": None, "status": "activo"}
    ]

# Verifica que la funcion retorne las entidades con la descripcion mas larga
def test_orderEntitiesTest(originalEntitiesList):
    # Longitudes de las descripciones:
    # id = 5: "lentes para proteccion contra el sol" (36)
    # id = 3: "Protector solar resistente al agua" (34)
    # id = 2: "Toalla de microfibra" (20)
    # Los ids esperados en orden son: 3, 5, 2 en ese orden
    
    result = getListEntities(originalEntitiesList)
    
    # Verificar que el resultado tiene 3 elementos
    assert len(result) == 3
    
    # extraccion de los id de los objetos
    ids_expected = [5, 3, 2]
    ids_obtained = [item["id"] for item in result]
    # Verificar que las listas son iguales
    assert ids_obtained == ids_expected

# Comprueba el manejo de valores None (Nulls)
def test_noneValuesTest(originalEntitiesList):
    # añadimos un nuevo elemento a la lista y verificamos que la ordenacion funcione
    originalEntitiesList.append({"id": 8, "name": "test", "description": "Esta es la descripcion mas larga de todas las descripciones", "status": "activo"})
        # Los ids esperados en orden son: 8, 5, 3 en ese orden
    
    result = getListEntities(originalEntitiesList)
    
    assert result[0]["id"] == 8
    assert result[1]["id"] == 5
    assert result[2]["id"] == 3
    

# Se comprueba que lance el error de manera adecuada cuando pasamos un lista vacia
def test_emptyListTest():
    with pytest.raises(ValueError) as excinfo:
        getListEntities([])
    assert "La lista esta vacía" in str(excinfo.value)

# Verificamos que se lance error para una lista con menos de 3 elementos
def test_lessThanThreeElementsTest():
    smallList = [{"id": 1, "description": "primer elemento"}, {"id": 2, "description": "segundo elemento"}]
    with pytest.raises(ValueError) as excinfo:
        getListEntities(smallList)
    assert "La lista debe de contener a lo menos 3 elementos" in str(excinfo.value)

# Comprueba que la lista original no haya sido mutada
def test_noMutationTest(originalEntitiesList):
    originalList = list(originalEntitiesList) 
    getListEntities(originalEntitiesList)
    
    # La lista no tiene que ser modificada
    assert originalEntitiesList == originalList
    