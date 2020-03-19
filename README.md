# Crear un base de datos


**Crer la Database:** Es un archivo cual contiene todos los datos.

```python
connect = sqlite3.connect("database.db")
```

**Crear una Tabla:** Crear una tabla

```python

cursor.execute("""CREATE TABLE product
                  (name text, business text, price int, 
                   quantity int, comment text)""")
```

**Enviar un Consulta:**

```python
consulta = db.cursor()
consulta.execute("select * from tabla")
```

**Seguridad:** El ataque mas comun para las base de datos es **Sql injection** que es un procedimiento donde un cliente inserta datos fraudulentos para conseguir privilegios que pueden ser 

* Eliminar la base de datos
* Cambiar valores de la base de datos
* Recibir datos prohibidos

para evitar el ataque sql injection se debe usar un comparador de **contenido** en el caso que utilize el ```==```  usted tiene un enorme fallo de seguridad.

### ¿Porque es un agujero de seguridad usar ```==``` ?
Porque es un operador que compara la direccion de memoria ram de un objeto no compara la informacion que contiene la variable.

**Comparador de contenido para una consulta correcta**
 
 ```java
        if(mensaje.equals("contenido"))
        {
           System.out.println("El contenido de los mensajes son iguales");
        }
 
```


# Imagen en funcionamiento

![alt text](https://github.com/IDiegoUlises/Crea-una-Base-de-Datos/blob/master/images/database.png)








