# Crear un base de datos


**Crer la Database:** Crea un archivo el cual contiene nuestros datos.

```python
connect = sqlite3.connect("database.db")
```

**Crear una Tabla:** Crear una tabla que contiene los detalles de un producto o servicio.

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

**Seguridad:** El ataque mas comun a la base de datos es **SQL INYECCTOR** que se base en que el usuario cambia los valores de una consulta para 

* Eliminar la base de datos
* Cambiar valores de la base de datos
* Recibir datos prohibidos.

para evitar esto debe usar un comparador de **contenido**  en el caso que utilize ```==```  usted tiene un enorme fallo de seguridad.

### ¿Porque es un agujero de seguridad el ```==``` ?
Porque es un operador que compara la direccion de memoria ram del objeto no compara por el valor que contiene la variable.

**Comparador de contenido para una consulta correcta**
 
 ```java
        if(mensaje.equals("contenido"))
        {
           System.out.println("El contenido de los mensajes son iguales");
        }
 
```


# Imagen en funcionamiento

![alt text](https://github.com/IDiegoUlises/Crea-una-Base-de-Datos/blob/master/images/database.png)








